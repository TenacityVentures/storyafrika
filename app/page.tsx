"use client"

import { useEffect, useRef, useState } from "react"
import Image from "next/image"
import { AnimatePresence, motion } from "framer-motion"

export default function WaitList() {
  const [imagePositions, setImagePositions] = useState<{ x: number; y: number }[]>([])
  const [idleOffsets, setIdleOffsets] = useState<{ x: number; y: number }[]>([])
  const [hasMounted, setHasMounted] = useState(false)
  const [currentSlide, setCurrentSlide] = useState<number>(0)
  const [email, setEmail] = useState("")
  const [joinedCount, setJoinedCount] = useState<number>(() => {
    if (typeof window !== "undefined") {
      const stored = window.localStorage.getItem("waitlistCount")
      return stored ? parseInt(stored) || 137 : 137
    }
    return 137
  })
  const containerRef = useRef<HTMLDivElement>(null)
  const mouseRef = useRef({
    x: 0,
    y: 0,
    targetX: 0,
    targetY: 0,
    smoothX: 0,
    smoothY: 0,
  })
  const animationFrameRef = useRef<number | null>(null)

  const photoCards = [
    {
      id: 1,
      src: "https://images.unsplash.com/photo-1521295121783-8a321d551ad2?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Gaming",
      speed: 130,
      className: "top-[-40%] left-[1%] w-[320px] h-[200px]",
    },
    {
      id: 2,
      src: "https://images.unsplash.com/photo-1546551142-ce1d774e630a?q=80&w=1025&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Office",
      speed: 160,
      className: "top-[-50%] left-[55%] w-[250px] h-[350px]",
    },
    {
      id: 3,
      src: "https://images.unsplash.com/photo-1487546331507-fcf8a5d27ab3?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Sunset",
      speed: 120,
      className: "top-[-35%] right-[10%] w-[300px] h-[220px]",
    },
    {
      id: 4,
      src: "https://images.unsplash.com/photo-1610441572339-bdf395d1c410?q=80&w=1025&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Young Teenager Africans in the beach",
      speed: 170,
      className: "top-[-55%] right-[65%] w-[200px] h-[280px]",
    },
    {
      id: 5,
      src: "https://images.unsplash.com/photo-1615156803802-c95ce44447d1?q=80&w=705&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Gamer",
      speed: 115,
      className: "top-[-15%] right-[-35%] w-[340px] h-[220px]",
    },
    {
      id: 6,
      src: "https://images.unsplash.com/photo-1763347120836-5afd4a60fc01?q=80&w=764&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "African Girl",
      speed: 145,
      className: "top-[25%] right-[-45%] w-[280px] h-[200px]",
    },
    {
      id: 7,
      src: "https://images.unsplash.com/photo-1687422808277-2334638f09fb?q=80&w=1054&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Gaming 2",
      speed: 125,
      className: "top-[55%] right-[-40%] w-[300px] h-[180px]",
    },
    {
      id: 8,
      src: "https://images.unsplash.com/photo-1681545303529-b6beb2e19f02?q=80&w=1158&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Office 2",
      speed: 145,
      className: "bottom-[-45%] right-[25%] w-[280px] h-[350px]",
    },
    {
      id: 9,
      src: "https://images.unsplash.com/photo-1586348943529-beaae6c28db9?q=80&w=715&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Sunset 2",
      speed: 110,
      className: "bottom-[-38%] left-[55%] w-[320px] h-[220px]",
    },
    {
      id: 10,
      src: "https://images.unsplash.com/photo-1703248187500-bc92a1e83f53?q=80&w=736&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "African Butterfly",
      speed: 155,
      className: "bottom-[-50%] left-[8%] w-[250px] h-[300px]",
    },
    {
      id: 11,
      src: "https://images.unsplash.com/photo-1509099836639-18ba1795216d?q=80&w=1031&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Gamer 2",
      speed: 120,
      className: "bottom-[20%] left-[-40%] w-[340px] h-[220px]",
    },
    {
      id: 12,
      src: "https://images.unsplash.com/photo-1521884189581-a6ede70026ea?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "People 2",
      speed: 140,
      className: "top-[35%] left-[-42%] w-[300px] h-[200px]",
    },
    {
      id: 13,
      src: "https://images.unsplash.com/photo-1588349242964-28b720afcb36?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "African Kids Playing",
      speed: 165,
      className: "top-[-10%] left-[-48%] w-[280px] h-[180px]",
    },
    {
      id: 14,
      src: "https://images.unsplash.com/photo-1507461476191-0ed4f9f18533?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Office 3",
      speed: 105,
      className: "top-[-60%] left-[35%] w-[260px] h-[330px]",
    },
    {
      id: 15,
      src: "https://images.unsplash.com/photo-1557050543-4d5f4e07ef46?q=80&w=1332&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Nature 3",
      speed: 150,
      className: "bottom-[-42%] right-[60%] w-[240px] h-[290px]",
    },
    {
      id: 16,
      src: "https://images.unsplash.com/photo-1720005979515-60f2fa091fad?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "People 3",
      speed: 128,
      className: "bottom-[50%] right-[-38%] w-[310px] h-[210px]",
    },
    {
      id: 17,
      src: "https://images.unsplash.com/photo-1612373931332-9fbb9b2290a1?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Gamer 3",
      speed: 138,
      className: "bottom-[-55%] left-[75%] w-[330px] h-[190px]",
    },
    {
      id: 18,
      src: "https://images.unsplash.com/photo-1577896849786-738ed6c78bd3?q=80&w=2074&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Gaming 4",
      speed: 118,
      className: "top-[60%] left-[-35%] w-[300px] h-[200px]",
    },
    {
      id: 19,
      src: "https://images.unsplash.com/photo-1595157724160-4aca7d33ea23?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Sunset 3",
      speed: 152,
      className: "top-[-45%] right-[-30%] w-[290px] h-[230px]",
    },
    {
      id: 20,
      src: "https://images.unsplash.com/photo-1730995210182-e54599dd1f89?q=80&w=1099&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Office 4",
      speed: 122,
      className: "bottom-[10%] left-[-50%] w-[270px] h-[360px]",
    },
    {
      id: 21,
      src: "https://images.unsplash.com/photo-1598314661607-75c4f6836aca?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Main sunset",
      speed: 100,
      className: "top-[28%] left-[8%] w-[320px] h-[240px]",
      hasOverlay: true,
    },
    {
      id: 22,
      src: "https://images.unsplash.com/photo-1523805009345-7448845a9e53?q=80&w=1172&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Main office",
      speed: 95,
      className: "top-[12%] right-[10%] w-[280px] h-[380px]",
    },
    {
      id: 23,
      src: "https://images.unsplash.com/photo-1553775927-a071d5a6a39a?q=80&w=1087&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      alt: "Main gamer",
      speed: 105,
      className: "bottom-[18%] right-[8%] w-[340px] h-[220px]",
    },
  ]

  useEffect(() => {
    const initialPositions = photoCards.map(() => ({ x: 0, y: 0 }))
    setImagePositions(initialPositions)
    setIdleOffsets(photoCards.map(() => ({ x: 0, y: 0 })))

    const revealTimer = setTimeout(() => setHasMounted(true), 150)
    return () => clearTimeout(revealTimer)
  }, [])

  useEffect(() => {
    const makeZeroOffsets = () => photoCards.map(() => ({ x: 0, y: 0 }))

    let resetTimeout: number | null = null
    const triggerJitter = () => {
      setIdleOffsets(
        photoCards.map(() => ({
          x: (Math.random() - 0.5) * 24,
          y: (Math.random() - 0.5) * 24,
        })),
      )

      resetTimeout = window.setTimeout(() => {
        setIdleOffsets(makeZeroOffsets())
      }, 2200)
    }

    const initialKick = window.setTimeout(triggerJitter, 2600)
    const interval = window.setInterval(triggerJitter, 7800)

    return () => {
      window.clearTimeout(initialKick)
      window.clearInterval(interval)
      if (resetTimeout) window.clearTimeout(resetTimeout)
    }
  }, [])

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      const mouse = mouseRef.current
      const centerX = window.innerWidth / 2
      const centerY = window.innerHeight / 2

      mouse.targetX = (e.clientX - centerX) / centerX
      mouse.targetY = (e.clientY - centerY) / centerY
    }

    const animate = () => {
      const mouse = mouseRef.current

      const smoothFactor = 0.1
      mouse.smoothX += (mouse.targetX - mouse.smoothX) * smoothFactor
      mouse.smoothY += (mouse.targetY - mouse.smoothY) * smoothFactor

      setImagePositions((prev) =>
        prev.map((pos, index) => {
          const card = photoCards[index]

          const easeFactor = 0.05 + (index % 5) * 0.015

          const targetX = -mouse.smoothX * card.speed * 5
          const targetY = -mouse.smoothY * card.speed * 5

          return {
            x: pos.x + (targetX - pos.x) * easeFactor,
            y: pos.y + (targetY - pos.y) * easeFactor,
          }
        }),
      )

      animationFrameRef.current = requestAnimationFrame(animate)
    }

    window.addEventListener("mousemove", handleMouseMove)
    animationFrameRef.current = requestAnimationFrame(animate)

    return () => {
      window.removeEventListener("mousemove", handleMouseMove)
      if (animationFrameRef.current) {
        cancelAnimationFrame(animationFrameRef.current)
      }
    }
  }, [])

  const nextSlide = () => {
    setCurrentSlide((s) => Math.min(s + 1, 3))
  }

  const joinWaitlist = (e: React.FormEvent) => {
    e.preventDefault()
    if (!email.trim()) return
    const newCount = joinedCount + 1
    setJoinedCount(newCount)
    try {
      window.localStorage.setItem("waitlistCount", String(newCount))
    } catch {}
    setCurrentSlide(3)
  }

  return (
    <div
      ref={containerRef}
      className="relative min-h-screen w-full overflow-hidden"
      style={{
        background: "linear-gradient(135deg, #1a4d4d 0%, #2d5a5a 30%, #7a6b4d 70%, #a67c52 100%)",
      }}
    >
      {photoCards.map((card, index) => {
        const position = imagePositions[index] || { x: 0, y: 0 }
        const idle = idleOffsets[index] || { x: 0, y: 0 }
        const angle = (index / photoCards.length) * Math.PI * 2
        const baseRadius = 200 // space images further apart from the center
        const baseOffsetX = Math.cos(angle) * baseRadius
        const baseOffsetY = Math.sin(angle) * baseRadius
        const translateX = position.x + baseOffsetX + idle.x
        const translateY = position.y + baseOffsetY + idle.y
        const distanceFromCenter = Math.sqrt(baseOffsetX * baseOffsetX + baseOffsetY * baseOffsetY)
        const rippleDelay = 0.45 + distanceFromCenter / 900
        return (
          <motion.div
            key={card.id}
            className={`absolute ${card.className} rounded-2xl overflow-hidden shadow-2xl`}
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{
              opacity: hasMounted ? 1 : 0,
              scale: hasMounted ? 1 : 0.9,
              x: translateX,
              y: translateY,
            }}
            transition={{
              delay: rippleDelay,
              opacity: { duration: 0.8 },
              scale: { type: "spring", stiffness: 160, damping: 18 },
              x: { type: "spring", stiffness: 80, damping: 20 },
              y: { type: "spring", stiffness: 80, damping: 20 },
            }}
            style={{ willChange: "transform" }}
          >
            <Image src={card.src || "/placeholder.svg"} alt={card.alt} fill className="object-cover" />
            {/*card.hasOverlay && (
              <div className="absolute top-4 left-4 right-4 backdrop-blur-xl bg-white/10 border border-white/20 rounded-full px-4 py-2 flex items-center gap-2">
                <div className="w-5 h-5 rounded-full bg-white/30 flex items-center justify-center text-xs">🔍</div>
                <span className="text-white text-sm font-medium">Amazing ocean sunset</span>
              </div>
            )*/}
          </motion.div>
        )
      })}

      <div className="relative z-10 flex min-h-screen items-center justify-center px-4">
        <AnimatePresence mode="wait">
          <motion.div
            key={currentSlide}
            initial={{ opacity: 0, y: 24, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -24, scale: 0.98 }}
            transition={{ type: "spring", stiffness: 300, damping: 30 }}
            className="w-full max-w-2xl rounded-[2.5rem] backdrop-blur-2xl bg-white/10 border border-white/20 shadow-2xl p-12 text-center"
            style={{
              transform: `translate(${(imagePositions[0]?.x || 0) * 0.15 + (idleOffsets[0]?.x || 0) * 0.08}px, ${(imagePositions[0]?.y || 0) * 0.15 + (idleOffsets[0]?.y || 0) * 0.08}px)`,
              willChange: "transform",
            }}
          >
            {currentSlide === 0 && (
              <div>
                <h1 className="text-5xl md:text-6xl font-bold text-white mb-8 leading-tight text-balance">
                  Africa has always been rich in stories.
                </h1>
                <button
                  onClick={nextSlide}
                  className="bg-white hover:bg-gray-100 text-gray-900 font-semibold text-lg px-12 py-4 rounded-full shadow-lg transition-all hover:scale-105 active:scale-95"
                >
                  Next
                </button>
              </div>
            )}

            {currentSlide === 1 && (
              <div>
                <h2 className="text-4xl md:text-5xl font-bold text-white mb-8 leading-tight text-balance">
                  What we lacked was preservation
                </h2>
                <button
                  onClick={nextSlide}
                  className="bg-white hover:bg-gray-100 text-gray-900 font-semibold text-lg px-12 py-4 rounded-full shadow-lg transition-all hover:scale-105 active:scale-95"
                >
                  Next
                </button>
              </div>
            )}

            {currentSlide === 2 && (
              <form onSubmit={joinWaitlist} className="space-y-6">
                <h3 className="text-3xl md:text-4xl font-semibold text-white leading-tight text-balance">
                  Join the waitlist
                </h3>
                <div className="flex items-center gap-3 mt-4">
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="you@example.com"
                    className="flex-1 px-5 py-4 rounded-full bg-white/20 border border-white/30 text-white placeholder:text-white/70 focus:outline-none focus:ring-2 focus:ring-white/60"
                    required
                  />
                  <button
                    type="submit"
                    className="bg-white hover:bg-gray-100 text-gray-900 font-semibold text-lg px-8 py-4 rounded-full shadow-lg transition-all hover:scale-105 active:scale-95"
                  >
                    Join
                  </button>
                </div>
                <button
                  type="button"
                  onClick={nextSlide}
                  className="mt-6 text-white/80 underline hover:text-white"
                >
                  Skip
                </button>
              </form>
            )}

            {currentSlide === 3 && (
              <div>
                <h4 className="text-3xl md:text-4xl font-semibold text-white mb-4">
                  Already joined: {joinedCount.toLocaleString()}
                </h4>
                <p className="text-white/80 mb-8 text-lg">
                  Thank you — we’re building a home for African stories.
                </p>
                <button
                  onClick={() => setCurrentSlide(0)}
                  className="bg-white hover:bg-gray-100 text-gray-900 font-semibold text-lg px-12 py-4 rounded-full shadow-lg transition-all hover:scale-105 active:scale-95"
                >
                  Restart
                </button>
              </div>
            )}
          </motion.div>
        </AnimatePresence>
      </div>

      
    </div>
  )
}