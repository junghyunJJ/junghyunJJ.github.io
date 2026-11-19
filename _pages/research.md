---
layout: page
title: Research
permalink: /research/
description: EHR foundation models, AI agents, spatial and single-cell omics, and integrative genomics.
nav: true
nav_order: 1
---

I develop EHR foundation models and AI agents at the intersection of computational biology and bioinformatics, working across clinical data, spatial omics, and genetics.

{% assign ehr_theme = site.data.home.research | where: "id", "ehr-foundation-models" %}
{% assign other_themes = site.data.home.research | where_exp: "theme", "theme.id != 'ehr-foundation-models'" %}
{% assign themes = ehr_theme | concat: other_themes %}
{% include research_cards.html detailed=true themes=themes %}

Several of these directions are supported by reusable software and analysis tools. See the [software page]({{ "/software/" | relative_url }}) for current projects.
