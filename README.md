# ⏰ Deadline Tracker

An AI-powered application built with Streamlit and Gemini Vision that parses messy real-world images (syllabi, schedules, assignment notices) to extract structured deadlines and dispatches reminders via Gmail or Telegram.

## Features
- **Visual Deadline Extraction**: Reads image-based schedules using Gemini Vision.
- **Graceful Failure Handling**: Safely detects non-schedule images.
- **Multi-Channel Alerts**: Send summary digests via Gmail (SMTP) or Telegram Bot.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/deadline-tracker.git](https://github.com/YOUR_USERNAME/deadline-tracker.git)
   cd deadline-tracker