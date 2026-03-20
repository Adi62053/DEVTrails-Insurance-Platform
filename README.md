# DEVTrails 2026 – AI-Powered Parametric Insurance for Food Delivery Partners

## Project Description
An AI‑driven platform that protects food delivery gig workers from income loss caused by external, uncontrollable events (extreme weather, curfews, app outages, etc.). The system uses **parametric triggers** to automatically initiate claims and payouts, ensuring zero‑touch, instant compensation for lost wages. Coverage strictly excludes health, accidents, and vehicle repairs, and is priced on a **weekly premium model** aligned with gig workers’ income cycles.

## Persona
**Food Delivery Partner** (e.g., Swiggy, Zomato, Uber Eats)

## Scenarios & Workflow
1. **User Onboarding** – Delivery partner signs up with phone number, delivery zone, and average daily earnings.
2. **Risk Profiling** – AI calculates a personalized weekly premium based on zone risk, historical claims, and season.
3. **Policy Purchase** – User pays the premium (mock payment) to activate coverage for the upcoming week.
4. **Trigger Monitoring** – Backend continuously monitors external APIs (weather, curfew alerts, app status).
5. **Automated Claim** – When a trigger condition is met (e.g., heavy rain in the user’s zone), a claim is automatically created.
6. **Fraud Detection** – AI checks for GPS spoofing, duplicate claims, and anomalies; if passed, claim is approved.
7. **Instant Payout** – Approved claim triggers a simulated payment to the user’s registered account.
8. **Dashboard** – User sees earnings protected, active coverage, and claim history; admin views loss ratios and fraud alerts.

## Weekly Premium Model
- **Base premium:** $5 per week (or local currency equivalent).
- **Risk multipliers:**
  - **Zone risk factor** (0–0.5) – based on historical claim frequency and weather patterns in the delivery zone.
  - **Individual claim history factor** (0–0.3) – increases if the user has claimed frequently in the past.
  - **Seasonal factor** (0–0.2) – e.g., monsoon season increases risk.
- **Formula:**  
  `weekly_premium = base * (1 + zone_factor) * (1 + user_factor) * (1 + seasonal_factor)`

## Parametric Triggers
| Trigger Name       | Condition                                      | Data Source              |
|--------------------|------------------------------------------------|--------------------------|
| Heavy Rain         | Rainfall > 20mm in a day                       | OpenWeatherMap (mock)    |
| Extreme Heat       | Temperature > 40°C                              | OpenWeatherMap (mock)    |
| Air Pollution      | AQI > 300                                       | OpenWeatherMap / AQICN   |
| Sudden Curfew      | Government‑imposed curfew in delivery zone      | Mock news API            |
| Low Visibility     | Visibility < 500m due to fog/smoke              | OpenWeatherMap (mock)    |

## Platform Choice
**Web Application** (responsive design for mobile devices)

## AI/ML Integration Plans
- **Dynamic Premium Calculation:** Initially rule‑based, later enhanced with a regression model (scikit‑learn) that learns from historical claim data and weather forecasts.
- **Fraud Detection:** Rule‑based checks (GPS location mismatch, duplicate claims, frequency anomalies). Optionally, an Isolation Forest model to detect unusual claim patterns.
- **Predictive Analytics:** Simple linear regression to forecast next week’s claim volume based on weather predictions, helping admins adjust risk pools.

## Tech Stack
- **Frontend:** React (with Tailwind CSS)
- **Backend:** Python (FastAPI)
- **Database:** PostgreSQL (managed via pgAdmin)
- **AI/ML:** Python microservice (FastAPI) with scikit‑learn
- **APIs:** OpenWeatherMap (mocked for development), custom mocks for curfew and app outage
- **Payment Mock:** Stripe sandbox / simulated endpoint
- **Scheduler:** APScheduler (for periodic trigger checks)
- **Version Control:** Git / GitHub

## Development Plan
### Phase 1 (Weeks 1–2) – Foundation ✅
- [x] GitHub repository created with detailed README.
- [x] Backend (FastAPI) initialized with database connection.
- [x] Frontend (React) scaffolded.
- [x] Database (PostgreSQL) set up and connected.
- [x] 2‑minute demo video recorded and linked below.

### Phase 2 (Weeks 3–4) – Core Features (Upcoming)
- [ ] User registration & authentication.
- [ ] Policy purchase with dynamic premium calculation (rule‑based).
- [ ] Trigger monitoring service (mock weather API).
- [ ] Automated claim creation and payout simulation.
- [ ] User dashboard (coverage, earnings protected).

### Phase 3 (Weeks 5–6) – Scale & Optimise
- [ ] Advanced fraud detection (GPS spoofing, duplicate claim checks).
- [ ] Admin dashboard (loss ratios, fraud alerts, predictive analytics).
- [ ] Instant payout integration (mock payment gateway).
- [ ] Final 5‑minute demo video and pitch deck.

## TRAM NAME
- CODE CORTEX
## Team Members
- ADITYA KUMAR - TEAM LEADER
- Saurabh Yadav - TECH SUPPORT
-kapa Anjali-Frontend Developer & Documentation Lead
-SHAIK MASTAN SAHEB - ML Engineer

## Links
- **GitHub Repository:** [https://github.com/Adi62053/DEVTrails-Insurance-Platform](https://github.com/Adi62053/DEVTrails-Insurance-Platform)
- **Phase 1 Demo Video:** [Add your video link here]

## Setup Instructions (for developers)

### Prerequisites
- Python 3.9+ installed
- Node.js 16+ and npm installed
- PostgreSQL installed and running

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Adi62053/DEVTrails-Insurance-Platform.git
   cd DEVTrails-Insurance-Platform/backend