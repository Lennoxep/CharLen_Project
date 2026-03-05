# Quick Figma Reference

A quick cheat sheet for converting Figma frames to React components.

## 🚀 Quick Start

1. **Open Figma** → Select your frame
2. **Open Inspect panel** (right sidebar) → Get measurements
3. **Copy template:**
   ```bash
   cp src/components/FIGMA_FRAME_TEMPLATE.jsx src/components/ui/YourComponent.jsx
   ```
4. **Match styles** using the conversions below
5. **Export assets** → `src/assets/`

## 📏 Common Conversions

### Spacing (Figma → Tailwind)
| Figma | Tailwind | Use Case |
|-------|----------|----------|
| 4px | `p-1`, `m-1`, `gap-1` | Tight spacing |
| 8px | `p-2`, `m-2`, `gap-2` | Small spacing |
| 16px | `p-4`, `m-4`, `gap-4` | Default spacing |
| 24px | `p-6`, `m-6`, `gap-6` | Medium spacing |
| 32px | `p-8`, `m-8`, `gap-8` | Large spacing |
| 48px | `p-12`, `m-12`, `gap-12` | Extra large |

### Border Radius
| Figma | Tailwind |
|-------|----------|
| 4px | `rounded` |
| 8px | `rounded-lg` |
| 12px | `rounded-xl` |
| 16px | `rounded-2xl` |
| 24px | `rounded-3xl` |
| 9999px | `rounded-full` |

### Typography
| Figma Size | Tailwind | Weight |
|------------|----------|--------|
| 12px | `text-xs` | `font-normal` |
| 14px | `text-sm` | `font-normal` |
| 16px | `text-base` | `font-normal` |
| 18px | `text-lg` | `font-medium` |
| 20px | `text-xl` | `font-semibold` |
| 24px | `text-2xl` | `font-bold` |
| 30px | `text-3xl` | `font-bold` |
| 36px | `text-4xl` | `font-bold` |

### Colors
- **Use design tokens:** `var(--color-primary)`
- **Or Tailwind:** `bg-black`, `text-gray-600`
- **Or exact:** `bg-[#646cff]`

### Layout
| Figma | Tailwind |
|-------|----------|
| Auto Layout (Horizontal) | `flex flex-row` |
| Auto Layout (Vertical) | `flex flex-col` |
| Gap | `gap-4` |
| Padding | `p-4` or `px-4 py-4` |
| Max Width Container | `max-w-5xl mx-auto` |

## 🎯 Component Checklist

When converting a Figma frame:

- [ ] Created component file in correct folder (`ui/`, `layout/`, `features/`)
- [ ] Matched container width/height
- [ ] Matched padding/margin
- [ ] Matched colors (use design tokens)
- [ ] Matched typography (size, weight, line-height)
- [ ] Matched border radius
- [ ] Exported images/icons to `src/assets/`
- [ ] Tested responsive (if Figma has breakpoints)
- [ ] Added hover states (if Figma has them)

## 📦 Exporting Assets

1. **Select element** in Figma
2. **Right-click → Export**
3. **Choose format:**
   - SVG for icons/logos
   - PNG for images with transparency
   - JPG for photos
4. **Save to:** `src/assets/`
5. **Import:**
   ```jsx
   import logo from './assets/logo.svg'
   ```

## 🔍 Figma Inspect Panel Tips

- **Width/Height:** Use exact values or Tailwind classes
- **Padding:** Convert to `p-*` or `px-* py-*`
- **Gap:** Use `gap-*` for flex/grid
- **Font:** Match size, weight, line-height
- **Color:** Copy hex code or use design tokens
- **Effects:** Shadows, blur → Tailwind shadow utilities

## 💡 Pro Tips

1. **Start with structure** - Match HTML hierarchy first
2. **Then add styles** - Apply Tailwind classes
3. **Use exact values** when needed: `w-[120px]` instead of forcing Tailwind
4. **Componentize early** - If you see it twice, make it a component
5. **Check responsive** - Figma often has mobile/tablet/desktop frames

## 📚 Full Guide

See `FIGMA_INTEGRATION.md` for the complete guide.
