# Feature Components

This folder contains feature-specific components for your application.

## Current Components

- `BookCard.jsx` - Displays a book with like/dislike functionality

## Adding New Feature Components from Figma

When you get a Figma frame for a feature-specific component:

1. **Create the component file:**
   ```
   BookList.jsx
   BookDetail.jsx
   UserProfile.jsx
   ```

2. **Match the Figma design:**
   - Use the same structure as the Figma frame
   - Match all measurements, colors, and typography
   - Export any images/icons to `src/assets/`

3. **Example:**
   ```jsx
   // BookList.jsx
   // Figma Frame: "Book List View"
   
   export default function BookList({ books }) {
     return (
       <div className="[Figma-matched container]">
         {books.map(book => (
           <BookCard key={book.id} book={book} />
         ))}
       </div>
     );
   }
   ```
