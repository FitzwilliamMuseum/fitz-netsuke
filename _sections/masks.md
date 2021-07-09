---
title: Mask Netsuke
layout: default
permalink: /sections/masks
order: 7
image: /images/thumbnails/O_98_2008.jpeg
---
Masks were used throughout Japanese culture in dance, theatrical performances and religion. Masks were an important type of netsuke and were usually copies of ancient masks, but many were from the carver's own whimsy and imagination.


<div class="row">
{% assign sorted-posts = site.explore | where: "section","7" | order: "order" %}
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
