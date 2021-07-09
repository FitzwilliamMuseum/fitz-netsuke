---
title: Manju Netsuke
layout: default
permalink: /sections/manju
order: 6
image: /images/thumbnails/O_48_1991.jpeg
---
A thick, flat, round form of netsuke, like the rice cake of the same name. The carving usually done in relief, sometimes made of two pieces of ivory.

<div class="row">
{% assign sorted-posts = site.explore | where: "section","6" | order: "order" %}
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
