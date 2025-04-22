# M&B Auto Body Shop Website

A modern, responsive website for M&B Auto Group's body shop business.

## Live Demo

View the live website at: https://YOUR-USERNAME.github.io/mnb-auto-body/

## Features

- Responsive design that works on all devices
- Modern and professional UI suitable for an auto body shop
- Interactive elements including testimonial slider
- Contact form for quote requests
- Service showcase
- Work gallery
- About section with company information
- Google Maps integration

## Project Structure

```
mnb-auto-body/
├── css/
│   └── styles.css
├── js/
│   └── script.js
├── images/
│   └── (image files)
└── index.html
```

## GitHub Pages Deployment

To deploy this website on GitHub Pages:

1. Create a new GitHub repository
2. Push this project to your repository:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/mnb-auto-body.git
   git push -u origin main
   ```
3. Go to your repository settings on GitHub
4. Navigate to "Pages" in the left sidebar
5. Under "Source", select "Deploy from a branch"
6. Select the "main" branch and "/ (root)" folder
7. Click "Save"
8. Your site will be published at `https://YOUR-USERNAME.github.io/mnb-auto-body/`

## Local Development

To run this website locally:

1. Clone the repository
2. Navigate to the project directory
3. Start a local server:
   ```
   python -m http.server 8000
   ```
   or
   ```
   python3 -m http.server 8000
   ```
4. Open your browser and go to `http://localhost:8000`

## Customization

### Images
For optimal display, use the following image dimensions:
- Hero background: 1920x1080px
- Gallery images: 600x400px
- About section image: 800x600px

### Content
- Update the contact information, address, and Google Maps embed code
- Customize the services, testimonials, and about section content
- Replace placeholder images with actual images of the body shop

## Technologies Used

- HTML5
- CSS3
- JavaScript (Vanilla)
- Font Awesome for icons
- Google Fonts (Montserrat and Roboto)

## Browser Compatibility

This website is compatible with:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Opera (latest)

## Notes for Production

Before final deployment:

1. Update the Google Maps embed with the actual shop location
2. Connect the contact form to a backend service or email system
3. Add any additional SEO meta tags as needed
4. Consider adding Google Analytics or similar tracking
