Video Playback Test
===================

The sections below try different approaches so you can see which works inside WeChat's in‑app browser.

Autoplay inline video (with poster)
-----------------------------------

.. raw:: html

   <div style="max-width:1080px;margin:1em auto;">
     <video autoplay muted playsinline loop poster="_static/images/putiBirol.png" style="width:100%;border-radius:12px;display:block;background:#000;">
       <source src="_static/videos/putiBirol.mp4" type="video/mp4">
       Your browser does not support the video tag.
     </video>
   </div>

Autoplay inline with tap overlay (WeChat friendly)
--------------------------------------------------

.. raw:: html

   <div style="position:relative;max-width:1080px;margin:1em auto;">
     <a href="_static/videos/putiBirol.mp4" style="position:absolute;inset:0;z-index:2;display:block;" aria-label="Open video"></a>
     <video autoplay muted playsinline loop poster="_static/images/putiBirol.png" style="width:100%;border-radius:12px;display:block;background:#000;">
       <source src="_static/videos/putiBirol.mp4" type="video/mp4">
     </video>
   </div>

Direct link fallback (opens system player)
-----------------------------------------

`Open the MP4 video <_static/videos/putiBirol.mp4>`_

GIF fallback (no tap needed, larger size)
----------------------------------------

.. image:: _static/images/PutiBirol_90.gif
   :alt: Animated preview
   :class: no-scaled-link
   :align: center

Static image + button
---------------------

.. raw:: html

   <div style="max-width:1080px;margin:1em auto;text-align:center;">
     <img src="_static/images/putiBirol.png" alt="Preview" style="width:100%;max-width:1080px;border-radius:12px;display:block;margin:0 auto;">
     <div style="margin-top:1em;">
       <a href="_static/videos/putiBirol.mp4" style="display:inline-block;padding:0.8em 1.4em;background:#27ae60;color:#fff;border-radius:8px;text-decoration:none;font-weight:600;">Watch the video</a>
     </div>
   </div>
