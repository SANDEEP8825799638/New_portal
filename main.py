from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    dummy_employee = {
        'Full_Name': 'Sandeep Vasan',
        'Job_Title': 'Lead Operations Engineer',
        'Employee_Number': 'EMP-2048',
        'Department': 'Plant Operations',
        'Date_Joined': '2024-02-01',
        'Reporting_To': 'Alex Morgan',
        'Business_Unit': 'Concrete OEM Unit A',
        'Cost_Center': 'CC-108',
        'Blood_Group': 'O+',
        'Emergency_Contact_Number': '+1 555-0199',
        'Work_Email': 'sandeep@concreteoem.local',
        'Mobile_Phone': '+1 555-0144'
    }

    dummy_reports = [
        {'route': '#', 'display_name': 'Daily Telemetry Log'},
        {'route': '#', 'display_name': 'Production Summary'},
    ]

    dummy_modules = [
        {'route': '#', 'display_name': 'Batch Mixing System'},
        {'route': '#', 'display_name': 'Quality Assurance Registry'},
        {'route': '#', 'display_name': 'Inventory & Material Dispatch'},
    ]

    dummy_subordinates = [
        {
            'Full_Name': 'Jane Carter',
            'Employee_Number': 'EMP-2091',
            'Job_Title': 'Field Technician',
            'Department': 'Plant Operations'
        },
        {
            'Full_Name': 'Marcus Vance',
            'Employee_Number': 'EMP-2104',
            'Job_Title': 'Junior Automation Tech',
            'Department': 'Plant Operations'
        }
    ]












    dummy_jd_html = """
    <p><strong>Role Summary:</strong> Responsible for orchestrating concrete batch workflows, maintaining plant equipment throughput, and monitoring real-time operational logs.</p>
    <ul>
        <li>Maintain minimum 98.5% plant uptime across operating shifts.</li>
        <li>Review subordinate diagnostic records daily.</li>
        <li>Execute scheduled macro pipelines via the operator dashboard.</li>
    </ul>
    """

    return render_template(
        'employee2.html',
        employee=dummy_employee,
        is_manager=True,
        manager_pending_total=2,
        reports=dummy_reports,
        modules=dummy_modules,
        subordinates=dummy_subordinates,
        html_output=dummy_jd_html
    )

@app.route('/company_directory')
def company_directory():
    employees = [
        {"id": "OEM-101", "name": "Sandeep Vasan", "role": "Operations Engineer", "department": "Plant Operations", "phone": "+1 555-0144"},
        {"id": "OEM-102", "name": "Alex Morgan", "role": "Operations Manager", "department": "Plant Operations", "phone": "+1 555-0199"},
        {"id": "OEM-103", "name": "Sarah Jenkins", "role": "Credit Controller", "department": "Credit Control", "phone": "+1 555-0182"},
        {"id": "OEM-104", "name": "David Kim", "role": "Accounts Lead", "department": "Finance & Accounts", "phone": "+1 555-0112"},
        {"id": "OEM-105", "name": "Priya Sharma", "role": "HR Generalist", "department": "HR & Attendance", "phone": "+1 555-0167"},
        {"id": "OEM-106", "name": "Michael Chang", "role": "QC Chemist", "department": "Quality Control", "phone": "+1 555-0138"}
    ]
    return render_template('company_directory.html', employees=employees)

@app.route('/announcements')
def announcements():
    announcement_list = [
        {
            "id": 1,
            "title": "Annual Scheduled Maintenance – Batching Plant A",
            "category": "Safety & Operations",
            "date": "Sep 12, 2026",
            "author": "Operations Control",
            "urgent": True,
            "summary": "Full power shutdown and equipment overhaul scheduled for Unit A this weekend. All personnel must follow standard lockout/tagout (LOTO) protocols.",
            "attachment": "Plant_A_Maintenance_Protocol.pdf"
        },
        {
            "id": 2,
            "title": "Upcoming Holiday Notice: Regional Festival",
            "category": "HR Notice",
            "date": "Sep 10, 2026",
            "author": "HR Department",
            "urgent": False,
            "summary": "Plant and office operations will remain closed next Monday. Emergency dispatch teams will be on rotational on-call shifts.",
            "attachment": None
        },
        {
            "id": 3,
            "title": "Q3 Production Milestone Achieved: 100,000 m³ Concrete Supplied",
            "category": "Company News",
            "date": "Sep 05, 2026",
            "author": "Executive Office",
            "urgent": False,
            "summary": "Congratulations to all field engineers, dispatch operators, and quality teams for crossing our Q3 dispatch targets two weeks ahead of schedule.",
            "attachment": None
        },
        {
            "id": 4,
            "title": "ERP System Upgrade Window – Sunday 10 PM to 2 AM",
            "category": "IT Updates",
            "date": "Sep 02, 2026",
            "author": "IT Infrastructure",
            "urgent": False,
            "summary": "The internal portal, billing service, and dispatch logging will undergo a routine server migration. Offline logging forms must be used during this period.",
            "attachment": "Offline_Log_Sheet.xlsx"
        }
    ]
    return render_template('announcements.html', announcements=announcement_list)

if __name__ == '__main__':
    app.run(debug=True)