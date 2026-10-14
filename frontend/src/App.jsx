import { useMemo, useState } from "react";

const API_URL = "http://127.0.0.1:8000/analyze";

const EXAMPLES = {
  "Bank Scam":
    "URGENT! Your bank account will be blocked today. Verify your account immediately by clicking this link and enter your OTP.",

  "Prize Scam":
    "Congratulations! You have won a cash prize of ₹50,000. Pay a small processing fee now to claim your reward.",

  "Delivery Scam":
    "Your parcel could not be delivered. Pay a small delivery fee and click this link to reschedule your shipment.",

  "Investment Scam":
    "Limited time investment opportunity! Invest now and get guaranteed returns. Double your money with our premium investment plan.",

  "Safe Message":
    "Hi, the project meeting is scheduled for tomorrow at 10 AM. Please bring the latest presentation and discuss the remaining tasks.",
};

const SIGNAL_INFO = {
  urgency: {
    label: "Urgency",
    description: "Pressure to act quickly or without thinking.",
  },
  threat: {
    label: "Threat",
    description: "Fear-based language involving blocking, penalties or consequences.",
  },
  financial_request: {
    label: "Financial Request",
    description: "The message asks for money, payment or financial information.",
  },
  credential_request: {
    label: "Credential Request",
    description: "The message asks for OTPs, passwords, PINs or other sensitive credentials.",
  },
  reward: {
    label: "Reward / Prize",
    description: "Unexpected rewards, prizes, lottery or cashback claims.",
  },
  authority_impersonation: {
    label: "Authority Claim",
    description: "The sender presents itself as a bank, government body or other authority.",
  },
  suspicious_link: {
    label: "Link Request",
    description: "The message encourages the user to click or visit a link.",
  },
  url_detected: {
    label: "URL Detected",
    description: "A web address was detected inside the message.",
  },
  investment_scam: {
    label: "Investment Pattern",
    description: "Investment-related language involving unusually attractive returns.",
  },
  job_scam: {
    label: "Job Scam Pattern",
    description: "Job or employment language associated with suspicious requests.",
  },
  delivery_scam: {
    label: "Delivery Pattern",
    description: "Delivery or parcel language associated with suspicious actions.",
  },
  loan_refund_scam: {
    label: "Loan / Refund Pattern",
    description: "Loan or refund claims combined with potentially suspicious actions.",
  },
};

const EVIDENCE_PATTERNS = [
  {
    type: "urgency",
    patterns: [
      "urgent",
      "urgently",
      "immediately",
      "act now",
      "right now",
      "today",
      "limited time",
      "last chance",
      "respond immediately",
      "without delay",
    ],
  },
  {
    type: "threat",
    patterns: [
      "account will be blocked",
      "account will be suspended",
      "account suspended",
      "blocked",
      "legal action",
      "penalty",
      "fine",
      "arrest",
      "account will be closed",
    ],
  },
  {
    type: "credential_request",
    patterns: [
      "otp",
      "one time password",
      "password",
      "pin",
      "cvv",
      "verification code",
      "login details",
      "credentials",
    ],
  },
  {
    type: "financial_request",
    patterns: [
      "send money",
      "transfer money",
      "make a payment",
      "pay now",
      "processing fee",
      "delivery fee",
      "bank details",
      "card details",
      "upi",
      "money",
      "deposit",
    ],
  },
  {
    type: "reward",
    patterns: [
      "you won",
      "you have won",
      "winner",
      "prize",
      "reward",
      "lottery",
      "cashback",
      "cash prize",
      "congratulations",
    ],
  },
  {
    type: "authority_impersonation",
    patterns: [
      "bank",
      "government",
      "income tax",
      "police",
      "customs",
      "official department",
      "customer support",
      "bank representative",
    ],
  },
  {
    type: "suspicious_link",
    patterns: [
      "http://",
      "https://",
      "www.",
      "click here",
      "click the link",
      "click this link",
      "verify here",
      "verify your account",
      "login here",
      "tap here",
    ],
  },
  {
    type: "investment_scam",
    patterns: [
      "investment opportunity",
      "invest now",
      "guaranteed returns",
      "guaranteed return",
      "guaranteed profit",
      "double returns",
      "double your money",
      "high returns",
      "quick returns",
    ],
  },
  {
    type: "job_scam",
    patterns: [
      "work from home job",
      "work from home",
      "job opportunity",
      "job offer",
      "selected for a job",
      "registration fee",
      "job registration",
      "employment opportunity",
    ],
  },
  {
    type: "delivery_scam",
    patterns: [
      "parcel could not be delivered",
      "delivery failed",
      "delivery is on hold",
      "reschedule your shipment",
      "reschedule delivery",
      "incorrect address",
      "address verification",
      "parcel is on hold",
      "package is on hold",
    ],
  },
  {
    type: "loan_refund_scam",
    patterns: [
      "loan application is approved",
      "loan approved",
      "loan processing fee",
      "your refund is ready",
      "receive the refund",
      "refund immediately",
    ],
  },
];

function RiskGauge({ score }) {
  const radius = 76;
  const circumference = 2 * Math.PI * radius;
  const progress = (score / 100) * circumference;

  return (
    <div className="risk-gauge">
      <svg viewBox="0 0 190 190" className="risk-gauge-svg">
        <circle
          className="gauge-track"
          cx="95"
          cy="95"
          r={radius}
        />

        <circle
          className="gauge-progress"
          cx="95"
          cy="95"
          r={radius}
          strokeDasharray={circumference}
          strokeDashoffset={circumference - progress}
        />
      </svg>

      <div className="gauge-content">
        <span className="gauge-score">{score}</span>
        <span className="gauge-label">RISK SCORE</span>
      </div>
    </div>
  );
}

function getRiskClass(level) {
  if (level === "HIGH") return "high";
  if (level === "MEDIUM") return "medium";
  return "low";
}

function getEvidence(text, indicators) {
  const lowerText = text.toLowerCase();
  const evidence = [];

  EVIDENCE_PATTERNS.forEach(({ type, patterns }) => {
    if (!indicators.includes(type)) return;

    patterns.forEach((pattern) => {
      const index = lowerText.indexOf(pattern.toLowerCase());

      if (index !== -1) {
        evidence.push({
          start: index,
          end: index + pattern.length,
          type,
          text: text.slice(index, index + pattern.length),
        });
      }
    });
  });

  const unique = [];
  const occupied = [];

  evidence
    .sort((a, b) => a.start - b.start)
    .forEach((item) => {
      const overlaps = occupied.some(
        ([start, end]) =>
          item.start < end && item.end > start
      );

      if (!overlaps) {
        unique.push(item);
        occupied.push([item.start, item.end]);
      }
    });

  return unique;
}

function HighlightedMessage({ text, indicators }) {
  const evidence = useMemo(
    () => getEvidence(text, indicators),
    [text, indicators]
  );

  if (!evidence.length) {
    return <div className="submitted-message">{text}</div>;
  }

  const pieces = [];
  let cursor = 0;

  evidence.forEach((item, index) => {
    if (item.start > cursor) {
      pieces.push(
        <span key={`text-${index}`}>
          {text.slice(cursor, item.start)}
        </span>
      );
    }

    pieces.push(
      <mark
        key={`mark-${index}`}
        className={`evidence-highlight ${item.type}`}
        title={SIGNAL_INFO[item.type]?.label || item.type}
      >
        {text.slice(item.start, item.end)}
      </mark>
    );

    cursor = item.end;
  });

  if (cursor < text.length) {
    pieces.push(
      <span key="text-end">{text.slice(cursor)}</span>
    );
  }

  return <div className="submitted-message">{pieces}</div>;
}

function App() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeMessage = async () => {
    const trimmedMessage = message.trim();

    if (!trimmedMessage) {
      setError("Please enter a message to analyze.");
      setResult(null);
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: trimmedMessage,
        }),
      });

      if (!response.ok) {
        throw new Error("Analysis request failed.");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(
        "Unable to connect to ScamLens. Make sure the FastAPI backend is running on port 8000."
      );
    } finally {
      setLoading(false);
    }
  };

  const loadExample = (exampleName) => {
    setMessage(EXAMPLES[exampleName]);
    setResult(null);
    setError("");
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    analyzeMessage();
  };

  const riskClass = result
    ? getRiskClass(result.risk_level)
    : "";

  return (
    <div className="app-shell">
      <div className="background-grid" />
      <div className="background-glow glow-one" />
      <div className="background-glow glow-two" />

      <header className="navbar">
        <div className="brand">
          <div className="brand-symbol">
            <span />
            <span />
            <span />
          </div>

          <div>
            <div className="brand-name">SCAMLENS</div>
            <div className="brand-subtitle">
              SCAM INTELLIGENCE PLATFORM
            </div>
          </div>
        </div>

        <nav className="nav-links">
          <a href="#analyzer">Analyzer</a>
          <a href="#how-it-works">How it works</a>
          <a href="#about">About</a>
        </nav>

        <div className="system-status">
          <span className="status-dot" />
          SYSTEM READY
        </div>
      </header>

      <main>
        <section className="hero">
          <div className="hero-copy">
            <div className="hero-eyebrow">
              <span className="eyebrow-line" />
              EXPLAINABLE SOCIAL-ENGINEERING ANALYSIS
            </div>

            <h1>
              DON’T TRUST.
              <br />
              <span>VERIFY.</span>
            </h1>

            <p className="hero-description">
              Analyze suspicious messages, identify manipulation
              signals, and understand exactly why a message may be
              dangerous.
            </p>

            <div className="hero-points">
              <span>Risk scoring</span>
              <span>Evidence detection</span>
              <span>Safety guidance</span>
            </div>
          </div>

          <div className="hero-product-panel">
            <div className="product-panel-line" />

            <div className="product-panel-content">
              <span className="mini-label">
                SCAMLENS / SECURITY INTELLIGENCE
              </span>

              <h2>
                Understand the
                <br />
                <span>risk before you act.</span>
              </h2>

              <p>
                A message can look legitimate and still use
                psychological pressure to influence your decision.
              </p>

              <div className="product-meta">
                <span>TEXT ANALYSIS</span>
                <span>RISK SCORING</span>
                <span>EXPLAINABLE RESULTS</span>
              </div>
            </div>
          </div>
        </section>

        <section className="analyzer-section" id="analyzer">
          <div className="section-heading">
            <div>
              <span className="section-kicker">01 / ANALYSIS</span>
              <h2>Analyze a suspicious message.</h2>
            </div>

            <p>
              Paste the message exactly as received. ScamLens
              evaluates language, contextual warning signals and
              suspicious requests.
            </p>
          </div>

          <form
            className="analyzer-card"
            onSubmit={handleSubmit}
          >
            <div className="analyzer-topbar">
              <div className="analyzer-title">
                <span className="terminal-dot" />
                MESSAGE ANALYZER
              </div>

              <span className="character-count">
                {message.length} / 5000
              </span>
            </div>

            <div className="message-input-container">
              <textarea
                value={message}
                onChange={(event) => {
                  setMessage(event.target.value);
                  setError("");
                }}
                placeholder="Paste a suspicious SMS, email, notification or social-media message here..."
                maxLength={5000}
                rows={8}
              />
            </div>

            <div className="analyzer-bottom">
              <div className="example-group">
                <span>TRY AN EXAMPLE</span>

                <div className="example-buttons">
                  {Object.keys(EXAMPLES).map((name) => (
                    <button
                      type="button"
                      key={name}
                      onClick={() => loadExample(name)}
                    >
                      {name}
                    </button>
                  ))}
                </div>
              </div>

              <button
                className="analyze-button"
                type="submit"
                disabled={loading}
              >
                {loading ? (
                  <>
                    <span className="button-spinner" />
                    ANALYZING...
                  </>
                ) : (
                  <>
                    ANALYZE MESSAGE
                    <span>→</span>
                  </>
                )}
              </button>
            </div>

            {error && (
              <div className="error-message">
                <span>!</span>
                {error}
              </div>
            )}
          </form>
        </section>

        {result && (
          <section className="result-section">
            <div className="result-header">
              <div>
                <span className="section-kicker">
                  02 / ASSESSMENT
                </span>

                <h2>Analysis complete.</h2>
              </div>

              <div className="processing-badge">
                ANALYZED IN {result.processing_time}s
              </div>
            </div>

            <div className="result-overview">
              <div className={`risk-panel ${riskClass}`}>
                <div className="risk-panel-label">
                  OVERALL RISK
                </div>

                <RiskGauge score={result.risk_score} />

                <div className="risk-level">
                  <span>{result.risk_level} RISK</span>
                </div>

                <p>
                  {result.risk_level === "HIGH"
                    ? "Multiple strong social-engineering indicators were detected."
                    : result.risk_level === "MEDIUM"
                    ? "Several warning signals were detected. Independent verification is recommended."
                    : "No major predefined social-engineering warning pattern was detected."}
                </p>
              </div>

              <div className="signals-panel">
                <div className="panel-heading">
                  <div>
                    <span className="mini-label">
                      SIGNAL ENGINE
                    </span>
                    <h3>Detected indicators</h3>
                  </div>

                  <span className="signal-count">
                    {result.indicators.length} SIGNALS
                  </span>
                </div>

                {result.indicators.length ? (
                  <div className="signals-grid">
                    {result.indicators.map((signal) => {
                      const info = SIGNAL_INFO[signal];

                      return (
                        <div
                          className="signal-card"
                          key={signal}
                        >
                          <div className="signal-card-top">
                            <span className="signal-indicator" />
                            <span>
                              {info?.label || signal}
                            </span>
                          </div>

                          <p>
                            {info?.description ||
                              "A predefined warning indicator was detected."}
                          </p>
                        </div>
                      );
                    })}
                  </div>
                ) : (
                  <div className="no-signals">
                    No major predefined warning signals were
                    detected.
                  </div>
                )}
              </div>
            </div>

            <div className="evidence-card">
              <div className="panel-heading">
                <div>
                  <span className="mini-label">
                    EVIDENCE LAYER
                  </span>
                  <h3>What triggered the assessment?</h3>
                </div>

                <span className="evidence-legend">
                  Highlighted text = detected evidence
                </span>
              </div>

              <div className="evidence-layout">
                <div className="message-evidence">
                  <div className="message-label">
                    SUBMITTED MESSAGE
                  </div>

                  <HighlightedMessage
                    text={result.message}
                    indicators={result.indicators}
                  />
                </div>

                <div className="explanation-box">
                  <div className="message-label">
                    EXPLANATION
                  </div>

                  <p>{result.explanation}</p>
                </div>
              </div>
            </div>

            <div className="recommendation-card">
              <div className="recommendation-heading">
                <div className="recommendation-icon">!</div>

                <div>
                  <span className="mini-label">
                    SAFETY RESPONSE
                  </span>
                  <h3>What should you do?</h3>
                </div>
              </div>

              <div className="recommendation-list">
                {result.recommendations.map(
                  (recommendation, index) => (
                    <div
                      className="recommendation-item"
                      key={index}
                    >
                      <span>✓</span>
                      <p>{recommendation}</p>
                    </div>
                  )
                )}
              </div>
            </div>
          </section>
        )}

        <section className="how-section" id="how-it-works">
          <div className="section-heading">
            <div>
              <span className="section-kicker">03 / WORKFLOW</span>
              <h2>From message to explainable risk.</h2>
            </div>

            <p>
              ScamLens is designed around a simple principle:
              detecting a threat is useful only when the user can
              understand it.
            </p>
          </div>

          <div className="workflow">
            <div className="workflow-step">
              <span>01</span>
              <div>
                <h3>Submit</h3>
                <p>
                  Paste the suspicious message exactly as received.
                </p>
              </div>
            </div>

            <div className="workflow-connector" />

            <div className="workflow-step">
              <span>02</span>
              <div>
                <h3>Analyze</h3>
                <p>
                  The analysis engine identifies contextual
                  manipulation signals.
                </p>
              </div>
            </div>

            <div className="workflow-connector" />

            <div className="workflow-step">
              <span>03</span>
              <div>
                <h3>Explain</h3>
                <p>
                  Evidence and contributing indicators are shown
                  directly from the submitted message.
                </p>
              </div>
            </div>

            <div className="workflow-connector" />

            <div className="workflow-step">
              <span>04</span>
              <div>
                <h3>Protect</h3>
                <p>
                  Practical safety recommendations help the user
                  decide what to do next.
                </p>
              </div>
            </div>
          </div>
        </section>

        <section className="about-section" id="about">
          <div className="about-card">
            <div>
              <span className="section-kicker">
                ABOUT SCAMLENS
              </span>

              <h2>
                Security decisions should be
                <span> understandable.</span>
              </h2>
            </div>

            <p>
              ScamLens is an explainable social-engineering scam
              risk assessment platform. Instead of only producing a
              scam or safe label, the system highlights the warning
              signals that influenced its assessment and provides
              practical safety guidance.
            </p>
          </div>
        </section>
      </main>

      <footer className="footer">
        <div className="brand footer-brand">
          <div className="brand-symbol small">
            <span />
            <span />
            <span />
          </div>

          <div>
            <div className="brand-name">SCAMLENS</div>
            <div className="brand-subtitle">
              EXPLAINABLE SCAM RISK ASSESSMENT
            </div>
          </div>
        </div>

        <p>
          Prototype for academic research and demonstration.
        </p>
      </footer>
    </div>
  );
}

export default App;