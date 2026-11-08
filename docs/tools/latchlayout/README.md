---
title: "LatchLayout workspace launcher"
category: "效率"
platforms: ["windows"]
tags: ["productivity", "automation"]
created: "2026-11-08"
updated: "2026-11-08"
---

# LatchLayout

Windows 11 x64 workspace launcher with a visual editor. Hold a configurable keyboard key or mouse button to open local applications, Chromium browser profiles, and HTTP(S) URLs on selected displays and full, half, or quarter layouts. This is an unsigned early preview.

## Features

- Named workspaces with hold durations from 0.5 to 10 seconds.
- Chrome profile-directory and URL configuration; optional isolated browser data directory.
- Per-window display selection and a live placement preview.
- Session reuse of created browser windows, manual startup, tray controls, and explicit Quit.
- MIT-licensed source; no key logging, telemetry, keyboard hooks, or app-owned network client.

## Installation

Tested platform: Windows 11 x64. Download `LatchLayout-win-x64.zip` and `SHA256SUMS.txt` from the [official release](https://github.com/stanczykwyatt/latchlayout/releases/tag/v0.2.0), verify the checksum, extract every file, and open `LatchLayout.exe`. The .NET runtime is included.

## Quick start

1. Edit a workspace and choose the hold input and duration.
2. Add a local executable; choose its display and layout. Browser mode accepts a profile folder and URLs.
3. Check the result with **Open workspace now**.
4. Enable hold shortcuts and hide to the tray. Quit stops the app completely.

The original key/mouse action remains active. Choose an input that will not disrupt typing or dragging. Imported configurations launch programs as your user; review and trust them before use.

## Verification and limits

30 local checks include native restoration on two displays and a real Chrome test with an isolated temporary profile. Physical input delivery, real sleep/resume, mixed-DPI hardware, monitor hot-plug, accessibility tools, Windows 10, and non-Chrome Chromium browsers have not been end-to-end verified. Concurrent external browser launches can make window attribution ambiguous. No independent security audit is claimed.

## Links

- [Source, documentation, and MIT license](https://github.com/stanczykwyatt/latchlayout)
- [Release](https://github.com/stanczykwyatt/latchlayout/releases/tag/v0.2.0)
- [Verification details](https://github.com/stanczykwyatt/latchlayout/blob/main/docs/VERIFICATION.md)
