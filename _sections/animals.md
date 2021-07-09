---
title: Animals
layout: default
permalink: /sections/animals
order: 2
image: /images/thumbnails/O_9_1917.jpeg
---
Like most animals in art history worldwide, the animals depicted in netsuke usually have symbolic meanings.

<div class="row">
{% assign sorted-posts = site.explore | where: "section","3" | order: "order" %}
{% for author in sorted-posts  %}
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
</div>
