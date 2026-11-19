import React from "react";

export const LogoMark = ({ className = "w-10 h-10" }) => (
  <svg
    viewBox="0 0 48 48"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    className={`${className} flex-shrink-0`}
    aria-label="DropGuard Academic Emblem"
  >
    <defs>
      {/* Background Crest Gradient: Royal Indigo to Deep Navy */}
      <linearGradient id="crestGrad" x1="4" y1="4" x2="44" y2="44" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stopColor="#4F46E5" />
        <stop offset="55%" stopColor="#3730A3" />
        <stop offset="100%" stopColor="#1E1B4B" />
      </linearGradient>

      {/* Mortarboard Diamond Gradient */}
      <linearGradient id="mortarGrad" x1="12" y1="12" x2="36" y2="24" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stopColor="#FFFFFF" />
        <stop offset="100%" stopColor="#E0E7FF" />
      </linearGradient>

      {/* Gold Academic Tassel */}
      <linearGradient id="goldGrad" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stopColor="#FDE047" />
        <stop offset="50%" stopColor="#F59E0B" />
        <stop offset="100%" stopColor="#D97706" />
      </linearGradient>

      {/* Emerald Retention Support Cradle */}
      <linearGradient id="emeraldGrad" x1="12" y1="28" x2="36" y2="38" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stopColor="#34D399" />
        <stop offset="100%" stopColor="#059669" />
      </linearGradient>
    </defs>

    {/* Outer Academic Shield Emblem */}
    <path
      d="M24 3.5 C34.5 3.5 42 7.2 42 16.5 C42 29.5 31.8 39.8 24 44.5 C16.2 39.8 6 29.5 6 16.5 C6 7.2 13.5 3.5 24 3.5 Z"
      fill="url(#crestGrad)"
    />

    {/* Subtle Inner Border */}
    <path
      d="M24 5.5 C33 5.5 39.8 8.8 39.8 16.8 C39.8 28.2 30.5 37.8 24 42 C17.5 37.8 8.2 28.2 8.2 16.8 C8.2 8.8 15 5.5 24 5.5 Z"
      stroke="#818CF8"
      strokeOpacity="0.4"
      strokeWidth="1"
    />

    {/* Academic Graduation Mortarboard Diamond */}
    <polygon
      points="24,12 36,17.2 24,22.4 12,17.2"
      fill="url(#mortarGrad)"
    />

    {/* Mortarboard Skullcap */}
    <path
      d="M17 19.4 V23 C17 25.2 20.1 27 24 27 C27.9 27 31 25.2 31 23 V19.4 L24 22.4 Z"
      fill="#C7D2FE"
    />

    {/* Academic Tassel & Golden Bead */}
    <path
      d="M24 17.2 L14.5 20.8 C14.2 22 14 24 14 25.5"
      stroke="url(#goldGrad)"
      strokeWidth="1.3"
      strokeLinecap="round"
    />
    <circle cx="14" cy="26" r="1.3" fill="url(#goldGrad)" />

    {/* Retention Cradle (Open Book of Knowledge) */}
    <path
      d="M23.5 35.8 C19.5 33.2 15.5 33.6 12.5 35.2 V28.8 C15.5 27.2 19.5 26.8 23.5 29.4 Z"
      fill="url(#emeraldGrad)"
    />
    <path
      d="M24.5 35.8 C28.5 33.2 32.5 33.6 35.5 35.2 V28.8 C32.5 27.2 28.5 26.8 24.5 29.4 Z"
      fill="url(#emeraldGrad)"
    />
    <path
      d="M24 28.5 V36.2"
      stroke="#FFFFFF"
      strokeWidth="1.2"
      strokeLinecap="round"
    />

    {/* Central Guidance Star */}
    <polygon
      points="24,24.8 25.2,27.2 27.8,27.2 25.7,28.7 26.5,31.1 24,29.5 21.5,31.1 22.3,28.7 20.2,27.2 22.8,27.2"
      fill="url(#goldGrad)"
    />
  </svg>
);

export const Logo = ({
  size = "md",
  showText = true,
  textVariant = "light",
  subtitle = "Student Retention System",
  className = "",
}) => {
  const sizeMap = {
    sm: "w-8 h-8",
    md: "w-10 h-10",
    lg: "w-12 h-12",
    xl: "w-16 h-16",
  };

  const markSize = sizeMap[size] || sizeMap.md;

  const isLightText = textVariant === "light";

  return (
    <div className={`flex items-center gap-3 ${className}`}>
      <div className="relative flex-shrink-0 drop-shadow-md">
        <LogoMark className={markSize} />
      </div>

      {showText && (
        <div className="flex flex-col overflow-hidden leading-tight">
          <span
            className={`font-extrabold tracking-tight ${
              size === "lg" || size === "xl" ? "text-xl sm:text-2xl" : "text-base sm:text-lg"
            } ${isLightText ? "text-white" : "text-slate-900"}`}
          >
            Drop<span className="text-indigo-400">Guard</span>
          </span>
          {subtitle && (
            <span
              className={`text-[10px] sm:text-[11px] font-semibold tracking-wider uppercase ${
                isLightText ? "text-indigo-200/80" : "text-slate-500"
              }`}
            >
              {subtitle}
            </span>
          )}
        </div>
      )}
    </div>
  );
};

export default Logo;
