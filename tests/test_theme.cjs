const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const test = require('node:test');

const source = fs.readFileSync(path.join(__dirname, '../assets/js/theme.js'), 'utf8');

function loadTheme(savedTheme, systemDark = false) {
  const attributes = new Map([['data-default-theme', 'dark'], ['data-theme', 'dark']]);
  const storage = new Map(savedTheme === undefined ? [] : [['theme', savedTheme]]);
  const highlights = {
    highlight_theme_light: { media: '' },
    highlight_theme_dark: { media: 'none' },
  };
  const context = vm.createContext({
    document: {
      documentElement: {
        getAttribute: key => attributes.get(key) ?? null,
        setAttribute: (key, value) => attributes.set(key, value),
        removeAttribute: key => attributes.delete(key),
        classList: { add() {}, remove() {} },
      },
      getElementById: id => highlights[id],
    },
    localStorage: {
      getItem: key => storage.get(key) ?? null,
      setItem: (key, value) => storage.set(key, String(value)),
    },
    window: {
      matchMedia: () => ({ matches: systemDark }),
      setTimeout: callback => callback(),
    },
  });
  vm.runInContext(source, context);
  return { context, attributes, storage, highlights };
}

test('a new visitor gets dark mode even when the OS prefers light', () => {
  const state = loadTheme();
  assert.equal(state.attributes.get('data-theme'), 'dark');
  assert.equal(state.highlights.highlight_theme_dark.media, '');
  assert.equal(state.highlights.highlight_theme_light.media, 'none');
});

test('an explicit light preference is preserved when the OS prefers dark', () => {
  const state = loadTheme('light', true);
  assert.equal(state.attributes.get('data-theme'), 'light');
});

test('legacy null and invalid preferences fall back to the site default', () => {
  for (const value of ['null', 'invalid']) {
    assert.equal(loadTheme(value).attributes.get('data-theme'), 'dark');
  }
});

test('the toggle changes the rendered theme and remembers the choice', () => {
  const state = loadTheme('dark');
  vm.runInContext('toggleTheme("dark")', state.context);
  assert.equal(state.attributes.get('data-theme'), 'light');
  assert.equal(state.storage.get('theme'), 'light');
  vm.runInContext('toggleTheme("light")', state.context);
  assert.equal(state.attributes.get('data-theme'), 'dark');
  assert.equal(state.storage.get('theme'), 'dark');
});
