Video Playback Test
===================

Video overlaid on GIF (auto-fallback)
---------------------------------------

If video doesn't play (like WeChat), GIF shows through underneath.

.. raw:: html

   <div style="position:relative;width:100%;max-width:1080px;margin:0 auto;overflow:hidden;aspect-ratio: 12 / 5;">
     <img src="_static/images/PutiBirol_slideshow.gif" alt="Fallback GIF" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;z-index:1;" />
     <video src="_static/videos/putiBirol_cropped.mov" autoplay loop muted playsinline style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;outline:0;background:transparent;object-fit:cover;z-index:2;">
     </video>
   </div>



