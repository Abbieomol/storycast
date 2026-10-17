# StoryCast

This is a three-page accessible microsite that shares short true stories from Kenya in audio and video. The stories are retold from publicly published Kenyan reporting . Built with plain HTML, Sass compiled to CSS, and no frameworks or JavaScript.

## Project structure

```
storycast/
  index.html                          Home
  about.html                          About / Access
  story/seven-hours-on-mount-kenya.html   Story detail page
  sass/                               main.scss + partials
    abstracts/  _layers, _colors, _typography, _spacing
    base/       _base (reset, base styles, focus, skip link)
    layout/     _layout (wrap, header, footer, grids)
    components/ _components (nav, buttons, media card, transcript...)
    utilities/  _utilities
  css/main.css                        compiled stylesheet
  assets/     audio/, video/, images/, captions/, transcripts/
  docs/       research document, sitemap and Figma links
```

## Run it locally

1. Open the folder in VS Code and use the Live Server extension, or run `python3 -m http.server 8000` in the folder and visit http://localhost:8000.
2. To change styles, install Sass (`npm install -g sass`) and run `sass --watch sass/main.scss:css/main.css`.
3. Add your media files before testing (see below).

## Files you need to add

In the HTML files, search for **ADD YOUR** to jump to each spot. Each one has a highlighted comment above it.

| Put this file in | Used on | Where in the HTML |
|---|---|---|
| `assets/images/hero.jpg` | Home | `<img class="hero__img">` in the hero |
| `assets/images/runner.jpg` | Home | first card in Featured stories |
| `assets/images/clinic.jpg` | Home and Story | "The Clinic That Was Not" card (decorative, empty alt) |
| `assets/images/skyline.jpg` | Home and Story | "The Nairobi Dream" card (decorative, empty alt) |
| `assets/video/seven-hours-on-mount-kenya.mp4` | Story | `<source>` inside `<video>` |
| `assets/audio/seven-hours-on-mount-kenya.mp3` | Story | `<audio>` in the sidebar |
| `assets/images/meeting.jpg` | About | image next to Our mission |

The captions (`assets/captions/*.vtt`) and the transcript are already included. Re-time the captions against your final video.

## Accessibility checklist

- [x] Semantic landmarks on every page: header, nav, main, footer, plus article, section, aside, figure
- [x] One h1 per page and headings in order
- [x] Skip link to main content on every page
- [x] Video has captions through a track element, a descriptive transcript and an audio-only version
- [x] No autoplay; native controls so media works with a keyboard
- [x] Visible focus outline (3 px) on all interactive elements, with a light outline on dark backgrounds
- [x] Colour contrast of 4.5:1 or higher for all text 
- [x] aria-current marks the current page in the navigation; ARIA is used only where needed
- [x] Responsive down to 320 px with Grid and Flexbox
- [x] Container query on the media card (stacked under 30 rem, horizontal at 30 rem and wider)
- [x] prefers-reduced-motion respected
- [ ] Final checks to do: axe and Lighthouse, keyboard-only test, screen reader test, caption timing

## Credits

All photos are free-licence images or my own. They are for illustration
only and do not show the real people or places named in the stories.

| File | Source link | 

| assets/images/hero.jpg | (https://www.facebook.com/MaiyanNanyuki/posts/with-the-recent-refreshing-rains-mt-kenyas-views-have-been-spectacular-the-crisp/970609575201782/)|
| assets/images/clinic.jpg |https://askannie.tortoisepath.com/hospital/nairobi-west-childrens-clinic/   | 
| assets/images/skyline.jpg | https://www.istockphoto.com/photos/nairobi-skyline | 
| assets/images/meeting.jpg |(https://www.linkedin.com/pulse/how-standout-group-discussion-chhandos-pramanik)| 

Story facts come from the references listed on the story page and in the research document.