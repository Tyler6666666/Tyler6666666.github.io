from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


OUTPUT_PATH = Path(r"C:\Users\pc\Desktop\My Resume\My Resume Final Outcomes.pdf")
LINK_COLOR = "#0B57D0"


def build_styles():
    styles = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=19,
            leading=22,
            alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.8,
            leading=11.8,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#333333"),
            spaceAfter=2,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=12,
            textColor=colors.HexColor("#111111"),
            spaceAfter=2,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.6,
            leading=12.1,
            alignment=TA_LEFT,
            spaceAfter=3,
        ),
        "entry_title": ParagraphStyle(
            "EntryTitle",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.9,
            leading=11.8,
            spaceAfter=1,
        ),
        "entry_body": ParagraphStyle(
            "EntryBody",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.25,
            leading=11.5,
            spaceAfter=2.5,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=11.6,
            leftIndent=12,
            firstLineIndent=-8,
            spaceAfter=1.2,
        ),
        "compact": ParagraphStyle(
            "Compact",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.15,
            leading=11.2,
            alignment=TA_LEFT,
            spaceAfter=2.5,
        ),
    }


def add_section(story, styles, title):
    story.append(Paragraph(title, styles["section"]))
    story.append(
        HRFlowable(
            width="100%",
            thickness=0.8,
            color=colors.HexColor("#666666"),
            spaceAfter=4,
            spaceBefore=0,
        )
    )


def add_bullets(story, styles, items):
    for item in items:
        story.append(Paragraph(f"&bull; {item}", styles["bullet"]))


def resolve_output_path():
    if not OUTPUT_PATH.exists():
        return OUTPUT_PATH

    try:
        with open(OUTPUT_PATH, "ab"):
            return OUTPUT_PATH
    except PermissionError:
        return OUTPUT_PATH.with_name("My Resume Final Outcomes v2.pdf")


def build_resume():
    styles = build_styles()
    output_path = resolve_output_path()
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=0.58 * inch,
        rightMargin=0.58 * inch,
        topMargin=0.48 * inch,
        bottomMargin=0.48 * inch,
    )

    story = []

    story.append(Paragraph("Tianren (Tyler) Zeng", styles["name"]))
    story.append(
        Paragraph(
            "Berkeley, CA | 949-678-3619 | tianren_zeng@berkeley.edu",
            styles["contact"],
        )
    )
    story.append(
        Paragraph(
            f'<font color="{LINK_COLOR}"><a href="https://github.com/Tyler6666666">github.com/Tyler6666666</a></font>'
            f' | <font color="{LINK_COLOR}"><a href="https://tyler6666666.github.io">tyler6666666.github.io</a></font>',
            styles["contact"],
        )
    )
    story.append(Spacer(1, 3))

    add_section(story, styles, "Summary")
    story.append(
        Paragraph(
            "UC Berkeley EECS junior focused on robotics, computer vision, and machine learning. "
            "Interested in autonomous systems, ROS2-based robot software, UAV perception and control, "
            "humanoid robot learning, and practical AI tools that turn domain workflows into usable software.",
            styles["body"],
        )
    )

    add_section(story, styles, "Education")
    story.append(
        Paragraph(
            "University of California, Berkeley | Berkeley, CA | EECS, Robotics Focus | Expected May 2027",
            styles["entry_title"],
        )
    )
    story.append(
        Paragraph(
            "Junior standing in Electrical Engineering and Computer Sciences with a technical focus on robotics, computer vision, and machine learning.",
            styles["entry_body"],
        )
    )
    story.append(
        Paragraph(
            "Irvine Valley College | Irvine, CA | Computer Science | May 2025",
            styles["entry_title"],
        )
    )
    story.append(
        Paragraph(
            "Completed lower-division coursework before transferring to UC Berkeley.",
            styles["entry_body"],
        )
    )

    add_section(story, styles, "Relevant Coursework")
    story.append(
        Paragraph(
            "<b>Spring 2026:</b> CS 189 Machine Learning | CS 188 Introduction to Artificial Intelligence | "
            "EECS 106A Introduction to Robotics | CS 61B Data Structures<br/>"
            "<b>Fall 2026:</b> EECS 127 Optimization Models in Engineering | ELENG C128 Feedback Control Systems",
            styles["compact"],
        )
    )

    add_section(story, styles, "Skills")
    story.append(
        Paragraph(
            "<b>Programming:</b> Python, Java, C++, C<br/>"
            "<b>Robotics:</b> ROS2 coding (Python), humanoid robot simulation environment setup, UAV drone simulation environment setup<br/>"
            "<b>AI / Vision:</b> Machine learning, computer vision, OpenCV, reinforcement learning<br/>"
            "<b>Web / Software:</b> TypeScript, React, Next.js, Tailwind CSS",
            styles["body"],
        )
    )

    add_section(story, styles, "Project Experience")
    story.append(
        Paragraph(
            f'Agent-HLE Task Proposal Agent | Next.js, TypeScript, React, Fuse.js, OpenRouter | 2026 | '
            f'<font color="{LINK_COLOR}"><a href="https://github.com/Tyler6666666/AgentHLE_task_proposal_agent.git">GitHub</a></font>',
            styles["entry_title"],
        )
    )
    add_bullets(
        story,
        styles,
        [
            "Built a web app that maps user professional backgrounds to Agent-HLE benchmark landscapes using keyword matching with LLM fallback, then generates customized task proposals.",
            "Implemented streaming proposal generation, review and refine workflows, and API-side safeguards such as rate limiting and structured fallback outputs.",
            "Outcome: delivered an end-to-end tool that turns a single user background prompt into benchmark-aligned task proposals with structured outputs and review support.",
        ],
    )

    story.append(
        Paragraph(
            f'BYOW Procedural Dungeon Game (CS61B Project 5) | Java | Spring 2026 | '
            f'<font color="{LINK_COLOR}"><a href="https://github.com/Tyler6666666/BYOW-build-your-own-world-">GitHub</a></font>',
            styles["entry_title"],
        )
    )
    add_bullets(
        story,
        styles,
        [
            "Developed a tile-based world generator with procedural room and hallway creation, HUD rendering, multiple difficulty settings, and save/load support.",
            "Added clickable path navigation, visibility mechanics, and monster/coin gameplay systems to support an interactive exploration experience.",
            "Outcome: shipped a playable Java dungeon game with deterministic world generation, interactive exploration, and persistent save/load gameplay.",
        ],
    )

    story.append(
        Paragraph(
            f'Flying Drone Tracking / Autonomous Drone Following | ROS2, Python, OpenCV | Spring 2026 | '
            f'<font color="{LINK_COLOR}"><a href="https://github.com/Tyler6666666/106a_final_project.git">GitHub</a></font> | '
            f'<font color="{LINK_COLOR}"><a href="https://cs106a-drone-convoy.vercel.app/">Website</a></font>',
            styles["entry_title"],
        )
    )
    add_bullets(
        story,
        styles,
        [
            "Built the ROS2 and Gazebo simulation environment for a leader-follower drone system, integrating perception, planning, and control modules end to end.",
            "Wrote the ArUco marker detection pipeline, tuned tracking and control parameters, and implemented low-level follower control for velocity matching and safe-distance behavior.",
            "Outcome: delivered a simulation testbed for autonomous drone following with target reacquisition under temporary occlusion before hardware deployment.",
        ],
    )

    add_section(story, styles, "Languages")
    story.append(
        Paragraph(
            "English: sufficient for academic and work settings<br/>"
            "Chinese: native speaker",
            styles["body"],
        )
    )

    doc.build(story)
    return output_path


if __name__ == "__main__":
    print(build_resume())
