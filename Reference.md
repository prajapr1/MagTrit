---
layout: default
title: Videos
---

# My Video Reference

<div id="youtube-gallery" style="max-width: 800px; margin: 0 auto;"></div>

<script>
  const videoUrls = [
    "https://youtu.be"
  ];

  function getYouTubeId(url) {
    const match = url.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/|v\/|shorts\/))([^&?\/]+)/);
    return match ? match : null;
  }

  const gallery = document.getElementById("youtube-gallery");

  videoUrls.forEach(url => {
    const id = getYouTubeId(url);
    if (!id) return;

    const wrapper = document.createElement("div");
    wrapper.style.cssText = "position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin-bottom: 24px;";

    wrapper.innerHTML = `
      <iframe 
        src="https://youtube.com{id}" 
        title="YouTube video player" 
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen>
      </iframe>
    `;

    gallery.appendChild(wrapper);
  });
</script>
