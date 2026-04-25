# How to Upload Card Images

## Option 1: Django Admin (Recommended)

1. Go to: `http://localhost:8000/admin/`
2. Login with your admin account
3. Click "Cards" under the "CARDS" section
4. Click on any card name to edit it
5. Scroll to "Card Image" section
6. Click "Choose File" to select an image from your computer
7. Image requirements:
   - Recommended size: 300x400px (portrait/card aspect ratio)
   - Supported formats: JPG, PNG, WebP, GIF
   - Max file size: Up to server limit (typically 5-100MB)
8. Click "Save" to upload and associate the image with the card

## Option 2: Bulk Upload

You can upload images for multiple cards:
1. Go to admin and edit each card one by one
2. Or use Django commands via terminal (advanced users)

## Image Placement

All uploaded images go to: `media/cards/`

The site automatically displays:
- Full image on the cards list page
- Thumbnail preview in admin list view
- Optimized for mobile and desktop viewing

## Notes

- Images are processed by Pillow (PIL) for optimization
- Django automatically handles file naming to prevent conflicts
- You can replace/update images anytime by editing the card
- If you delete an image from admin, it's removed from the server
