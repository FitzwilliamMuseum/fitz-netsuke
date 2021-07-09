---
title: Netsuke in the Fitzwilliam Collection
layout: default
---

<div class="container mb-3">
  <div class="row">
{% assign rows = site.sections.size | divided_by: 2.0 | ceil %}
{% for i in (1..rows) %}
{% assign offset = forloop.index0 | times: 2 %}
{% assign sorted = site.sections | sort:"order" %}
    {% for author in sorted limit:2 offset:offset %}
    <div class="col-md-4 mb-3">
      <div class="card h-100" >
        <a href="{{site.url}}{{site.baseurl}}{{ author.permalink }}" class="stretched-link">
          <img class="card-img-top" src="{{site.url}}{{site.baseurl}}{{author.image | replace: "large", "thumbnails" }}" alt="Thumbnail for {{author.title}}" width="300" height="300"/>
        </a>
        <div class="card-body">
          <h3 class="lead mt-2">
            <a href="{{site.url}}{{site.baseurl}}{{ author.permalink }}" class="stretched-link">{{author.title}}</a>
          </h3>
          <p class="text-info">{{author.objectID}}</p>
        </div>
      </div>
    </div>
    {% endfor %}
  {% endfor %}
  </div>
</div>
