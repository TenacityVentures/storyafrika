import type React from "react"
import type { Metadata, Viewport } from "next"
import { Geist, Geist_Mono } from "next/font/google"
import { Analytics } from "@vercel/analytics/next"
import "./globals.css"

const _geist = Geist({ subsets: ["latin"] })
const _geistMono = Geist_Mono({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "A digital home for African stories.",
  description: "StoryAfrika is Africa's digital storytelling home — preserving culture, history, and lived experiences through thoughtful, curated stories.",
  icons: {
    icon: [
      {
        url: "/logos/logo.jpg",
        media: "(prefers-color-scheme: light)",
      },
      {
        url: "/logos/logo-empty-bg.png",
        media: "(prefers-color-scheme: dark)",
      },
      {
        url: "/logos/logo.svg",
        type: "image/svg+xml",
      },
    ],
    apple: "/logos/logo.jpg",
  },
}

export const viewport: Viewport = {
  themeColor: "#0a0e1a",
  width: "device-width",
  initialScale: 1,
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body className={`font-sans antialiased`}>
        {children}
        <Analytics />
      </body>
    </html>
  )
}
