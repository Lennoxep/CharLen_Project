# Figma to React Integration Guide

This guide will help you import your Figma designs into this React project.

## 🎨 Before You Start Coding

### 1. **Extract Design Tokens from Figma**

When you get your Figma designs, extract these values:

#### Colors
- Open Figma → Select any element with a color
- Right-click the color → "Copy as CSS" or check the hex code
- Update `src/styles/design-tokens.css` with your colors

#### Typography
- Check Figma's Text Styles panel
- Note: font family, sizes, weights, line heights
- Update Tailwind config or design tokens file

#### Spacing
- Use Figma's spacing scale (if they have one)
- Common: 4px, 8px, 16px, 24px, 32px, 48px
- These map to Tailwind: `p-1`, `p-2`, `p-4`, `p-6`, `p-8`, `p-12`

#### Border Radius
- Check rounded corners in Figma
- Common: 4px, 8px, 12px, 16px, 9999px (full circle)

---

## 📦 Exporting Assets from Figma

### Images & Icons
1. **Select the element** in Figma
2. **Right-click → Export** (or use Export panel on the right)
3. **Choose format:**
   - **SVG** for icons/logos (scalable, small file size)
   - **PNG** for images with transparency
   - **JPG** for photos
4. **Save to:** `src/assets/` folder
5. **Import in code:**
   ```jsx
   import logo from './assets/logo.svg'
   <img src={logo} alt="Logo" />
   ```

### Fonts
- If Figma uses custom fonts (not system fonts):
  1. Download the font files (.woff2, .ttf)
  2. Add to `src/assets/fonts/`
  3. Import in `index.css`:
     ```css
     @font-face {
       font-family: 'YourFont';
       src: url('./assets/fonts/YourFont.woff2') format('woff2');
     }
     ```

---

## 🏗️ Building Components from Figma

### Step-by-Step Process

1. **Identify Components**
   - Look at your Figma frames
   - Each major section = a component
   - Reusable elements (buttons, cards) = separate components

2. **Create Component Structure**
   ```
   src/components/
     ├── ui/           # Buttons, inputs, cards
     ├── layout/       # Header, footer, navigation
     └── features/     # Feature-specific components
   ```

3. **Match Measurements**
   - Use Figma's **Inspect panel** (right sidebar)
   - See exact pixel values for:
     - Width/Height
     - Padding/Margin
     - Font sizes
     - Border radius
   - Convert to Tailwind classes or use exact values

4. **Example: Converting a Figma Button**
   
   **Figma specs:**
   - Width: 120px
   - Height: 40px
   - Padding: 12px 24px
   - Background: #646cff
   - Border radius: 8px
   - Font: 16px, weight 500
   
   **React code:**
   ```jsx
   <button className="w-[120px] h-[40px] px-6 py-3 bg-[#646cff] rounded-lg text-base font-medium">
     Click me
   </button>
   ```

---

## 🛠️ Useful Figma Plugins

Install these Figma plugins to make integration easier:

1. **Figma to React** - Generates React code from designs
2. **Figma to Code** - Exports HTML/CSS
3. **Design Tokens** - Extracts design system values
4. **Inspect** - Better measurement tools

---

## 📐 Common Figma → Tailwind Conversions

| Figma Value | Tailwind Class |
|------------|----------------|
| 4px | `p-1`, `m-1`, `gap-1` |
| 8px | `p-2`, `m-2`, `gap-2` |
| 16px | `p-4`, `m-4`, `gap-4` |
| 24px | `p-6`, `m-6`, `gap-6` |
| 32px | `p-8`, `m-8`, `gap-8` |
| 48px | `p-12`, `m-12`, `gap-12` |
| 4px radius | `rounded` |
| 8px radius | `rounded-lg` |
| 12px radius | `rounded-xl` |
| 9999px radius | `rounded-full` |

---

## ✅ Checklist When Importing a Design

- [ ] Extract all colors → Update `design-tokens.css`
- [ ] Export all images/icons → Save to `src/assets/`
- [ ] Note typography (fonts, sizes) → Update Tailwind config
- [ ] Create component structure matching Figma frames
- [ ] Match spacing using Tailwind classes
- [ ] Test responsive behavior (Figma has breakpoints too!)
- [ ] Verify hover states match Figma prototypes

---

## 💡 Pro Tips

1. **Start with the layout** - Build the overall page structure first
2. **Componentize early** - If you see the same element twice, make it a component
3. **Use Figma's Auto Layout** - It helps understand flexbox/grid
4. **Check responsive designs** - Figma often has mobile/tablet/desktop versions
5. **Match interactions** - If Figma has hover states, implement them in React

---

## 🚨 Common Pitfalls

- **Don't use exact pixel values everywhere** - Use Tailwind's responsive system
- **Don't forget hover/focus states** - Check Figma's interactive components
- **Don't hardcode colors** - Use your design tokens
- **Don't skip accessibility** - Add proper alt text, ARIA labels, etc.

---

## 📚 Resources

- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Figma to Code Tutorial](https://www.figma.com/community/plugin/747985167520967365/Figma-to-Code)
- [Design Tokens Guide](https://www.figma.com/community/plugin/888356646278934516/Design-Tokens)
