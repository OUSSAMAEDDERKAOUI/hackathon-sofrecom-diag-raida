"use client"

import { useEffect, useState } from "react"

export default function AILoadingPage() {
  const [dots, setDots] = useState("")

  useEffect(() => {
    const interval = setInterval(() => {
      setDots((prev) => (prev.length >= 3 ? "" : prev + "."))
    }, 500)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 flex items-center justify-center overflow-hidden">
      {/* Animated background gradient orbs */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-500/20 rounded-full blur-3xl animate-pulse" />
        <div
          className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-cyan-500/20 rounded-full blur-3xl animate-pulse"
          style={{ animationDelay: "1s" }}
        />
      </div>

      {/* Main content */}
      <div className="relative z-10 flex flex-col items-center justify-center gap-8">
        {/* Animated spinner */}
        <div className="relative w-24 h-24">
          <div className="absolute inset-0 rounded-full border-2 border-slate-700" />
          <div
            className="absolute inset-0 rounded-full border-2 border-transparent border-t-blue-500 border-r-cyan-500 animate-spin"
            style={{ animationDuration: "2s" }}
          />
          <div
            className="absolute inset-2 rounded-full border border-transparent border-t-blue-400 animate-spin"
            style={{ animationDuration: "3s", animationDirection: "reverse" }}
          />
        </div>

        {/* Text content */}
        <div className="text-center">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-3">
            <span className="bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
              AI Analyzing
            </span>
          </h1>
          <p className="text-lg text-slate-400 font-medium">Processing your request{dots}</p>
        </div>

        {/* Status indicators */}
        <div className="flex gap-4 mt-8">
          {[0, 1, 2].map((i) => (
            <div
              key={i}
              className="w-3 h-3 rounded-full bg-blue-500"
              style={{
                animation: "pulse 1.5s cubic-bezier(0.4, 0, 0.6, 1) infinite",
                animationDelay: `${i * 0.2}s`,
              }}
            />
          ))}
        </div>

        {/* Subtle description */}
        <p className="text-sm text-slate-500 mt-8 text-center max-w-sm">
          Advanced AI models are working to process your input and generate the best results
        </p>
      </div>

      {/* CSS for animations */}
      <style>{`
        @keyframes pulse {
          0%, 100% {
            opacity: 1;
          }
          50% {
            opacity: 0.5;
          }
        }
      `}</style>
    </div>
  )
}
