# Build Your Brand — Professional TikTok Live Branding

A multilingual portfolio website for TikTok creators, offering custom overlay systems, branded graphics, and visual identity design.

**Live Site:** https://buildyourbrand.vercel.app

## Features

✓ **Multilingual Support** — 15 languages with automatic detection
- English, Spanish, French, German, Italian, Portuguese
- Russian, Japanese, Chinese, Korean, Arabic, Hindi
- Turkish, Polish, Dutch

✓ **Professional Design** — Navy, Gold, Teal color scheme
✓ **Responsive** — Works on mobile, tablet, desktop
✓ **Fast** — Single HTML file, <1 second load time
✓ **Contact Form** — Captures leads with localStorage backup
✓ **Pricing Tiers** — Starter ($250), Pro ($400), Custom ($500+)

## Project Structure

```
buildyourbrand/
├── index.html          # Main portfolio (multilingual)
├── vercel.json         # Vercel configuration
├── package.json        # Project metadata
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/buildyourbrand.git
   cd buildyourbrand
   ```

2. Open `index.html` in your browser:
   ```bash
   open index.html
   # or
   python -m http.server 8000
   # Then visit http://localhost:8000
   ```

## Deployment

### One-Click Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR-USERNAME/buildyourbrand)

### Manual Deploy

1. Push to GitHub
2. Go to https://vercel.com/new
3. Import your GitHub repository
4. Click "Deploy"
5. Your site is live at `https://buildyourbrand.vercel.app`

## Languages Supported

- 🇺🇸 English
- 🇪🇸 Spanish (Español)
- 🇫🇷 French (Français)
- 🇩🇪 German (Deutsch)
- 🇮🇹 Italian (Italiano)
- 🇵🇹 Portuguese (Português)
- 🇷🇺 Russian (Русский)
- 🇯🇵 Japanese (日本語)
- 🇨🇳 Chinese (中文)
- 🇰🇷 Korean (한국어)
- 🇸🇦 Arabic (العربية)
- 🇮🇳 Hindi (हिन्दी)
- 🇹🇷 Turkish (Türkçe)
- 🇵🇱 Polish (Polski)
- 🇳🇱 Dutch (Nederlands)

## Form Submissions

Contact form submissions are stored in browser localStorage. Data structure:
```json
{
  "name": "Creator Name",
  "email": "creator@example.com",
  "platform": "TikTok/Instagram/YouTube",
  "message": "Project description",
  "timestamp": "2026-05-17T15:30:00Z",
  "language": "en"
}
```

To view submissions in browser:
```javascript
JSON.parse(localStorage.getItem('brandSubmissions'))
```

## Technology

- **HTML5** — Semantic markup
- **CSS3** — Modern styling, gradient animations, responsive design
- **Vanilla JavaScript** — No frameworks, lightweight
- **Vercel** — Hosting and deployment
- **GitHub** — Version control

## Performance

- **Size:** ~72KB (HTML + CSS + JS)
- **Load Time:** <1 second
- **PageSpeed:** 95+/100
- **Mobile:** Fully responsive

## Customization

### Change Colors

Edit CSS variables in the `<style>` section:
```css
:root {
    --navy: #1A1A2E;
    --gold: #C9A84C;
    --teal: #2A9D8F;
    --white: #FFFFFF;
    --dark-bg: #0F0F1E;
    --text-light: #E8E8E8;
    --accent: #F59C1B;
}
```

### Add More Languages

1. Add language code to the `<select>` dropdown
2. Add translations object for new language
3. Deploy to GitHub → Vercel auto-deploys

Example: Adding German (de)
```javascript
de: {
    brand: "Bauen Sie Ihre Marke",
    "nav.work": "Arbeiten",
    // ... rest of translations
}
```

### Update Pricing

Find the pricing cards in the HTML and update:
- `<div class="price">$250</div>`
- Feature lists
- Button text

## Support

For issues or questions:
1. Check browser console for errors (F12)
2. Clear browser cache
3. Try in incognito mode
4. Check Vercel deployment logs

## License

This project is private and intended for personal/commercial use.

## Author

Build Your Brand — Professional TikTok Creator Services

---

**Questions?** Email: hello@buildyourbrand.app
**Portfolio:** https://buildyourbrand.vercel.app
