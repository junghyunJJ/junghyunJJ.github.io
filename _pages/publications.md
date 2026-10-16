---
layout: page
permalink: /publications/
title: Publications
description: Publications, preprints, and ongoing manuscripts in computational biology and AI.
nav: true
nav_order: 2
scholar:
  bibliography_group_tag: h3
---

<div class="publications">

{% assign manuscripts = site.data.manuscripts.ongoing | concat: site.data.manuscripts.preprints %}
{% assign public_preprints = manuscripts | where_exp: "work", "work.paper_url != nil" | sort: "preprint_date" | reverse %}
{% assign unreleased = manuscripts | where_exp: "work", "work.paper_url == nil" %}
{% assign in_preparation = unreleased | where: "status", "In preparation" %}
{% assign other_manuscripts = unreleased | where_exp: "work", "work.status != 'In preparation'" %}
{% assign manuscripts = public_preprints | concat: in_preparation | concat: other_manuscripts %}
{% include manuscript_list.html id="ongoing-manuscripts" heading="Preprints & ongoing work" status="Under review" works=manuscripts %}

<section id="published-work" aria-labelledby="published-articles">
<h2 class="publication-section-title" id="published-articles">Published articles</h2>

{% bibliography --group_by year --group_order descending %}

</section>
</div>
