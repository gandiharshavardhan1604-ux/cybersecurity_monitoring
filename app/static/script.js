// ==========================================
// Load Dashboard Statistics
// ==========================================

async function loadStats() {

    try {

        const response = await fetch("/dashboard/stats");

        const data = await response.json();

        document.getElementById("total-events").textContent =
            data.total_events;

        document.getElementById("total-alerts").textContent =
            data.total_alerts;

        document.getElementById("critical-alerts").textContent =
            data.critical_alerts;

        document.getElementById("high-alerts").textContent =
            data.high_alerts;

    } catch (error) {

        console.error(
            "Error loading dashboard statistics:",
            error
        );

    }
}


// ==========================================
// Load Recent Security Alerts
// ==========================================

async function loadAlerts() {

    try {

        const response = await fetch("/alerts");

        const data = await response.json();

        const table =
            document.getElementById("alerts-table");

        table.innerHTML = "";

        data.alerts.forEach(alert => {

            const row =
                document.createElement("tr");

            row.innerHTML = `

                <td>${alert.id}</td>

                <td>
                    <strong>${alert.risk_level}</strong>
                </td>

                <td>${alert.threat}</td>

                <td>${alert.reason}</td>

                <td>${alert.created_at}</td>

            `;

            table.appendChild(row);

        });

    } catch (error) {

        console.error(
            "Error loading alerts:",
            error
        );

    }
}


// ==========================================
// Load All Security Events
// ==========================================

async function loadEvents() {

    try {

        const response = await fetch("/events");

        const data = await response.json();

        const table =
            document.getElementById("events-table");

        table.innerHTML = "";

        data.events.forEach(event => {

            const row =
                document.createElement("tr");

            row.innerHTML = `

                <td>${event.id}</td>

                <td>${event.event_type}</td>

                <td>${event.username}</td>

                <td>${event.ip_address}</td>

                <td>${event.message}</td>

                <td>${event.created_at}</td>

            `;

            table.appendChild(row);

        });

    } catch (error) {

        console.error(
            "Error loading security events:",
            error
        );

    }
}


// ==========================================
// Analyze Security Event
// ==========================================

document
    .getElementById("analyze-form")
    .addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            const eventType =
                document.getElementById("event_type").value;


            const username =
                document.getElementById("username").value;


            const ipAddress =
                document.getElementById("ip_address").value;


            const message =
                document.getElementById("message").value;


            const resultBox =
                document.getElementById("analysis-result");


            resultBox.innerHTML =
                "<p>Analyzing security event...</p>";


            try {

                const response =
                    await fetch("/analyze", {

                        method: "POST",

                        headers: {
                            "Content-Type": "application/json"
                        },

                        body: JSON.stringify({

                            event_type: eventType,

                            username: username,

                            ip_address: ipAddress,

                            message: message

                        })

                    });


                const data =
                    await response.json();


                if (!response.ok) {

                    throw new Error(
                        data.detail ||
                        "Analysis failed"
                    );

                }


                const analysis =
                    data.analysis;


                resultBox.innerHTML = `

                    <div class="result-row">

                        <strong>Risk Level:</strong>

                        <span class="risk-${analysis.risk_level.toLowerCase()}">

                            ${analysis.risk_level}

                        </span>

                    </div>


                    <div class="result-row">

                        <strong>Suspicious:</strong>

                        ${analysis.suspicious}

                    </div>


                    <div class="result-row">

                        <strong>Threat:</strong>

                        ${analysis.threat}

                    </div>


                    <div class="result-row">

                        <strong>Reason:</strong>

                        ${analysis.reason}

                    </div>


                    <div class="result-row">

                        <strong>Recommended Action:</strong>

                        ${analysis.recommended_action}

                    </div>


                    <div class="result-row">

                        <strong>AI Analysis:</strong>

                        <p>
                            ${analysis.llm_analysis}
                        </p>

                    </div>

                `;


                // ==========================================
                // Refresh Dashboard Data
                // ==========================================

                loadStats();

                loadAlerts();

                loadEvents();


                // ==========================================
                // Clear Form
                // ==========================================

                document
                    .getElementById("analyze-form")
                    .reset();


            } catch (error) {

                resultBox.innerHTML = `

                    <p>

                        Error analyzing event:
                        ${error.message}

                    </p>

                `;


                console.error(error);

            }

        }
    );


// ==========================================
// Load Dashboard When Page Opens
// ==========================================

loadStats();

loadAlerts();

loadEvents();
