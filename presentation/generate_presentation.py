"""
Generate Employee_Attrition_Model_Project_Presentation.pptx
Professional 16:9 widescreen academic & technical presentation with embedded speaker notes.
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

from slides_data import SLIDES_DATA

# Color Palette (Corporate Modern)
DARK_NAVY = RGBColor(15, 23, 42)      # #0F172A
SLATE_HEADER = RGBColor(30, 41, 59)   # #1E293B
INDIGO_PRIMARY = RGBColor(79, 70, 229) # #4F46E5
PURPLE_ACCENT = RGBColor(147, 51, 234) # #9333EA
EMERALD_SUCCESS = RGBColor(16, 185, 129) # #10B981
ROSE_ALERT = RGBColor(244, 63, 94)    # #F43F5E
AMBER_WARN = RGBColor(245, 158, 11)   # #F59E0B
LIGHT_BG = RGBColor(248, 250, 252)    # #F8FAFC
CARD_BG = RGBColor(255, 255, 255)     # #FFFFFF
BORDER_COLOR = RGBColor(226, 232, 240)# #E2E8F0
TEXT_DARK = RGBColor(30, 41, 59)      # #1E293B
TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B
TEXT_WHITE = RGBColor(255, 255, 255)  # #FFFFFF
HEADER_BAND = RGBColor(241, 245, 249) # #F1F5F9


def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]  # Blank slide layout

    for slide_info in SLIDES_DATA:
        slide = prs.slides.add_slide(blank_layout)
        slide_num = slide_info["slide_num"]

        # Embed Speaker Notes
        if "notes" in slide_info:
            notes_slide = slide.notes_slide
            notes_tf = notes_slide.notes_text_frame
            notes_tf.text = slide_info["notes"]

        if slide_num == 1:
            render_title_slide(slide, slide_info)
        else:
            render_standard_slide(slide, slide_info)

    output_path = os.path.join(os.path.dirname(__file__), "Employee_Attrition_Model_Project_Presentation.pptx")
    prs.save(output_path)
    print(f"SUCCESS: Created presentation at {output_path}")
    return output_path


def add_header_and_footer(slide, title_text, subtitle_text, slide_num):
    # Top Header Banner
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    # Title
    p_title = tf.paragraphs[0]
    p_title.text = title_text
    p_title.font.name = "Calibri"
    p_title.font.size = Pt(24)
    p_title.font.bold = True
    p_title.font.color.rgb = SLATE_HEADER

    # Subtitle
    if subtitle_text:
        p_sub = tf.add_paragraph()
        p_sub.text = subtitle_text
        p_sub.font.name = "Calibri"
        p_sub.font.size = Pt(12)
        p_sub.font.color.rgb = INDIGO_PRIMARY
        p_sub.space_before = Pt(3)

    # Accent divider line under header
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.03))
    line.fill.solid()
    line.fill.fore_color.rgb = INDIGO_PRIMARY
    line.line.color.rgb = INDIGO_PRIMARY

    # Footer
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.35))
    ft_tf = footer_box.text_frame
    ft_tf.word_wrap = True
    ft_tf.margin_left = ft_tf.margin_top = ft_tf.margin_right = ft_tf.margin_bottom = 0

    p_ft = ft_tf.paragraphs[0]
    p_ft.text = f"Employee Attrition Model  |  Final Year Project Viva  |  Candidate: Prithvi Raghuwanshi  |  Slide {slide_num} of 22"
    p_ft.font.name = "Calibri"
    p_ft.font.size = Pt(9.5)
    p_ft.font.color.rgb = TEXT_MUTED


def render_title_slide(slide, info):
    # Dark modern gradient-like background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = DARK_NAVY
    bg.line.fill.background()

    # Decorative accent card
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.0), Inches(11.333), Inches(5.5))
    card.fill.solid()
    card.fill.fore_color.rgb = RGBColor(30, 41, 59)
    card.line.color.rgb = RGBColor(51, 65, 85)

    # Title & Subtitle box
    tb = slide.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.333), Inches(2.2))
    tf = tb.text_frame
    tf.word_wrap = True

    p_badge = tf.paragraphs[0]
    p_badge.text = "FINAL YEAR MAJOR PROJECT PRESENTATION  •  ACADEMIC YEAR 2025–2026"
    p_badge.font.name = "Calibri"
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = INDIGO_PRIMARY

    p_title = tf.add_paragraph()
    p_title.text = info["title"]
    p_title.font.name = "Calibri"
    p_title.font.size = Pt(36)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE
    p_title.space_before = Pt(8)

    p_sub = tf.add_paragraph()
    p_sub.text = info["subtitle"]
    p_sub.font.name = "Calibri"
    p_sub.font.size = Pt(15)
    p_sub.font.color.rgb = RGBColor(148, 163, 184)
    p_sub.space_before = Pt(8)

    # Candidate and Institutional details in two columns
    details_box = slide.shapes.add_textbox(Inches(1.5), Inches(3.9), Inches(10.333), Inches(2.2))
    dtf = details_box.text_frame
    dtf.word_wrap = True

    for bullet in info["bullets"]:
        p = dtf.add_paragraph()
        p.text = "•  " + bullet
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.color.rgb = RGBColor(226, 232, 240)
        p.space_before = Pt(6)


def render_standard_slide(slide, info):
    # Add common header and footer
    add_header_and_footer(slide, info["title"], info.get("subtitle", ""), info["slide_num"])

    content_type = info.get("content_type", "")

    if content_type == "cards":
        render_cards_layout(slide, info["cards"])
    elif content_type == "table":
        render_table_layout(slide, info["headers"], info["rows"])
    elif content_type == "bullets_with_metrics":
        render_bullets_metrics_layout(slide, info["metrics"], info["bullets"])
    elif content_type == "comparison_cards":
        render_comparison_cards(slide, info["implemented"], info["future_scope"])
    elif content_type == "architecture_diagram":
        render_architecture_layout(slide, info["components"])
    elif content_type == "workflow_steps":
        render_workflow_steps(slide, info["steps"])
    elif content_type == "three_pillars":
        render_three_pillars(slide, info["pillars"])
    elif content_type == "pipeline_cards":
        render_pipeline_cards(slide, info["cards"])
    elif content_type == "metrics_grid":
        render_metrics_grid(slide, info["metrics"], info["matrix"])
    elif content_type == "ui_cards":
        render_ui_cards(slide, info["interfaces"])
    elif content_type == "conclusion_summary":
        render_conclusion_summary(slide, info["takeaways"])
    else:
        render_generic_bullets(slide, info.get("bullets", []))


def render_cards_layout(slide, cards):
    # 2x2 or 4-row grid of structured cards
    num_cards = len(cards)
    if num_cards == 4:
        coords = [
            (Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.3)),
            (Inches(6.8), Inches(1.8), Inches(5.6), Inches(2.3)),
            (Inches(0.8), Inches(4.4), Inches(5.6), Inches(2.3)),
            (Inches(6.8), Inches(4.4), Inches(5.6), Inches(2.3))
        ]
        for i, card in enumerate(cards):
            left, top, width, height = coords[i]
            shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
            shape.fill.solid()
            shape.fill.fore_color.rgb = LIGHT_BG
            shape.line.color.rgb = BORDER_COLOR

            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_top = tf.margin_left = tf.margin_right = tf.margin_bottom = 0

            p_title = tf.paragraphs[0]
            p_title.text = card["title"]
            p_title.font.name = "Calibri"
            p_title.font.size = Pt(15)
            p_title.font.bold = True
            p_title.font.color.rgb = INDIGO_PRIMARY

            p_desc = tf.add_paragraph()
            p_desc.text = card["desc"]
            p_desc.font.name = "Calibri"
            p_desc.font.size = Pt(12)
            p_desc.font.color.rgb = TEXT_DARK
            p_desc.space_before = Pt(6)


def render_table_layout(slide, headers, rows):
    num_rows = len(rows) + 1
    num_cols = len(headers)

    table_shape = slide.shapes.add_table(num_rows, num_cols, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.8))
    table = table_shape.table

    # Format Header Row
    for col_idx, header_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = header_text
        cell.fill.solid()
        cell.fill.fore_color.rgb = SLATE_HEADER
        for p in cell.text_frame.paragraphs:
            p.font.name = "Calibri"
            p.font.size = Pt(12)
            p.font.bold = True
            p.font.color.rgb = TEXT_WHITE

    # Format Data Rows
    for row_idx, row_data in enumerate(rows):
        for col_idx, val in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.text = str(val)
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT_BG if row_idx % 2 == 0 else CARD_BG
            for p in cell.text_frame.paragraphs:
                p.font.name = "Calibri"
                p.font.size = Pt(11)
                p.font.color.rgb = TEXT_DARK
                if col_idx == 0:
                    p.font.bold = True


def render_bullets_metrics_layout(slide, metrics, bullets):
    # Top 3 metric KPI boxes
    metric_width = Inches(3.7)
    gap = Inches(0.3)
    for i, m in enumerate(metrics):
        left = Inches(0.8) + i * (metric_width + gap)
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.8), metric_width, Inches(1.5))
        box.fill.solid()
        box.fill.fore_color.rgb = LIGHT_BG
        box.line.color.rgb = INDIGO_PRIMARY

        tb = slide.shapes.add_textbox(left + Inches(0.15), Inches(1.9), metric_width - Inches(0.3), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = m["label"]
        p1.font.name = "Calibri"
        p1.font.size = Pt(11)
        p1.font.color.rgb = TEXT_MUTED

        p2 = tf.add_paragraph()
        p2.text = m["value"]
        p2.font.name = "Calibri"
        p2.font.size = Pt(22)
        p2.font.bold = True
        p2.font.color.rgb = ROSE_ALERT

        p3 = tf.add_paragraph()
        p3.text = m["desc"]
        p3.font.name = "Calibri"
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = TEXT_DARK

    # Bottom detailed bullets
    bottom_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.6), Inches(11.733), Inches(3.0))
    bottom_box.fill.solid()
    bottom_box.fill.fore_color.rgb = CARD_BG
    bottom_box.line.color.rgb = BORDER_COLOR

    tb_b = slide.shapes.add_textbox(Inches(1.0), Inches(3.8), Inches(11.333), Inches(2.6))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True

    for i, bullet in enumerate(bullets):
        p = tf_b.add_paragraph() if i > 0 else tf_b.paragraphs[0]
        p.text = "•  " + bullet
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)


def render_comparison_cards(slide, implemented, future):
    # Left Card: Implemented Scope
    left_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.8))
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = LIGHT_BG
    left_card.line.color.rgb = EMERALD_SUCCESS

    tb_left = slide.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.4))
    tf_l = tb_left.text_frame
    tf_l.word_wrap = True

    p_h1 = tf_l.paragraphs[0]
    p_h1.text = "✔ FULLY IMPLEMENTED & VERIFIED"
    p_h1.font.name = "Calibri"
    p_h1.font.size = Pt(14)
    p_h1.font.bold = True
    p_h1.font.color.rgb = EMERALD_SUCCESS

    for item in implemented:
        p = tf_l.add_paragraph()
        p.text = "• " + item
        p.font.name = "Calibri"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(4)

    # Right Card: Future Scope
    right_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = LIGHT_BG
    right_card.line.color.rgb = PURPLE_ACCENT

    tb_right = slide.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.4))
    tf_r = tb_right.text_frame
    tf_r.word_wrap = True

    p_h2 = tf_r.paragraphs[0]
    p_h2.text = "⚡ PLANNED FUTURE ENHANCEMENTS"
    p_h2.font.name = "Calibri"
    p_h2.font.size = Pt(14)
    p_h2.font.bold = True
    p_h2.font.color.rgb = PURPLE_ACCENT

    for item in future:
        p = tf_r.add_paragraph()
        p.text = "• " + item
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)


def render_architecture_layout(slide, components):
    tier_height = Inches(1.05)
    gap = Inches(0.18)

    for i, c in enumerate(components):
        top = Inches(1.8) + i * (tier_height + gap)
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, Inches(11.733), tier_height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = LIGHT_BG
        shape.line.color.rgb = INDIGO_PRIMARY

        tb = slide.shapes.add_textbox(Inches(1.0), top + Inches(0.1), Inches(11.333), tier_height - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = f"{c['tier']}  —  {c['tech']}"
        p1.font.name = "Calibri"
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = INDIGO_PRIMARY

        p2 = tf.add_paragraph()
        p2.text = c["role"]
        p2.font.name = "Calibri"
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_DARK
        p2.space_before = Pt(3)


def render_workflow_steps(slide, steps):
    step_width = Inches(11.733)
    step_height = Inches(0.85)
    gap = Inches(0.12)

    for i, s in enumerate(steps):
        top = Inches(1.8) + i * (step_height + gap)
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, step_width, step_height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = LIGHT_BG
        shape.line.color.rgb = BORDER_COLOR

        tb = slide.shapes.add_textbox(Inches(1.0), top + Inches(0.1), Inches(11.333), step_height - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = f"{s['step']}:  {s['detail']}"
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK


def render_three_pillars(slide, pillars):
    width = Inches(3.7)
    gap = Inches(0.3)

    for i, p in enumerate(pillars):
        left = Inches(0.8) + i * (width + gap)
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.8), width, Inches(4.8))
        box.fill.solid()
        box.fill.fore_color.rgb = LIGHT_BG
        box.line.color.rgb = INDIGO_PRIMARY

        tb = slide.shapes.add_textbox(left + Inches(0.2), Inches(2.0), width - Inches(0.4), Inches(4.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p_title = tf.paragraphs[0]
        p_title.text = p["title"]
        p_title.font.name = "Calibri"
        p_title.font.size = Pt(15)
        p_title.font.bold = True
        p_title.font.color.rgb = INDIGO_PRIMARY

        for f in p["features"]:
            p_f = tf.add_paragraph()
            p_f.text = "• " + f
            p_f.font.name = "Calibri"
            p_f.font.size = Pt(11.5)
            p_f.font.color.rgb = TEXT_DARK
            p_f.space_before = Pt(8)


def render_pipeline_cards(slide, cards):
    card_width = Inches(2.18)
    gap = Inches(0.2)

    for i, c in enumerate(cards):
        left = Inches(0.8) + i * (card_width + gap)
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.8), card_width, Inches(4.8))
        box.fill.solid()
        box.fill.fore_color.rgb = LIGHT_BG
        box.line.color.rgb = BORDER_COLOR

        tb = slide.shapes.add_textbox(left + Inches(0.12), Inches(2.0), card_width - Inches(0.24), Inches(4.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p_title = tf.paragraphs[0]
        p_title.text = c["title"]
        p_title.font.name = "Calibri"
        p_title.font.size = Pt(13)
        p_title.font.bold = True
        p_title.font.color.rgb = INDIGO_PRIMARY

        p_desc = tf.add_paragraph()
        p_desc.text = c["desc"]
        p_desc.font.name = "Calibri"
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = TEXT_DARK
        p_desc.space_before = Pt(8)


def render_metrics_grid(slide, metrics, matrix):
    # Left column: Key Metrics
    metric_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(6.8), Inches(4.8))
    metric_box.fill.solid()
    metric_box.fill.fore_color.rgb = LIGHT_BG
    metric_box.line.color.rgb = BORDER_COLOR

    tb_m = slide.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(6.4), Inches(4.4))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True

    p_head = tf_m.paragraphs[0]
    p_head.text = "EMPIRICAL MODEL EVALUATION (HELD-OUT TEST SET)"
    p_head.font.name = "Calibri"
    p_head.font.size = Pt(13)
    p_head.font.bold = True
    p_head.font.color.rgb = INDIGO_PRIMARY

    for m in metrics:
        p = tf_m.add_paragraph()
        p.text = f"• {m['name']}: {m['val']} — {m['desc']}"
        p.font.name = "Calibri"
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # Right column: Confusion Matrix visualization
    mat_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.9), Inches(1.8), Inches(4.6), Inches(4.8))
    mat_box.fill.solid()
    mat_box.fill.fore_color.rgb = LIGHT_BG
    mat_box.line.color.rgb = BORDER_COLOR

    tb_mat = slide.shapes.add_textbox(Inches(8.1), Inches(2.0), Inches(4.2), Inches(4.4))
    tf_mat = tb_mat.text_frame
    tf_mat.word_wrap = True

    p_mhead = tf_mat.paragraphs[0]
    p_mhead.text = matrix["title"]
    p_mhead.font.name = "Calibri"
    p_mhead.font.size = Pt(13)
    p_mhead.font.bold = True
    p_mhead.font.color.rgb = SLATE_HEADER

    p_tn = tf_mat.add_paragraph()
    p_tn.text = f"True Negatives (Stayed & Predicted Stayed): {matrix['tn']}"
    p_tn.font.name = "Calibri"
    p_tn.font.size = Pt(11)
    p_tn.font.color.rgb = EMERALD_SUCCESS
    p_tn.space_before = Pt(12)

    p_fp = tf_mat.add_paragraph()
    p_fp.text = f"False Positives (Stayed & Predicted Left): {matrix['fp']}"
    p_fp.font.name = "Calibri"
    p_fp.font.size = Pt(11)
    p_fp.font.color.rgb = AMBER_WARN
    p_fp.space_before = Pt(8)

    p_fn = tf_mat.add_paragraph()
    p_fn.text = f"False Negatives (Left & Predicted Stayed): {matrix['fn']}"
    p_fn.font.name = "Calibri"
    p_fn.font.size = Pt(11)
    p_fn.font.color.rgb = ROSE_ALERT
    p_fn.space_before = Pt(8)

    p_tp = tf_mat.add_paragraph()
    p_tp.text = f"True Positives (Left & Predicted Left): {matrix['tp']}"
    p_tp.font.name = "Calibri"
    p_tp.font.size = Pt(11)
    p_tp.font.bold = True
    p_tp.font.color.rgb = INDIGO_PRIMARY
    p_tp.space_before = Pt(8)


def render_ui_cards(slide, interfaces):
    coords = [
        (Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.3)),
        (Inches(6.8), Inches(1.8), Inches(5.6), Inches(2.3)),
        (Inches(0.8), Inches(4.4), Inches(5.6), Inches(2.3)),
        (Inches(6.8), Inches(4.4), Inches(5.6), Inches(2.3))
    ]

    for i, ui in enumerate(interfaces):
        left, top, width, height = coords[i]
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = LIGHT_BG
        shape.line.color.rgb = INDIGO_PRIMARY

        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p_name = tf.paragraphs[0]
        p_name.text = ui["name"]
        p_name.font.name = "Calibri"
        p_name.font.size = Pt(15)
        p_name.font.bold = True
        p_name.font.color.rgb = INDIGO_PRIMARY

        p_desc = tf.add_paragraph()
        p_desc.text = ui["highlights"]
        p_desc.font.name = "Calibri"
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_DARK
        p_desc.space_before = Pt(8)


def render_conclusion_summary(slide, takeaways):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.8))
    shape.fill.solid()
    shape.fill.fore_color.rgb = LIGHT_BG
    shape.line.color.rgb = INDIGO_PRIMARY

    tb = slide.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(11.133), Inches(4.4))
    tf = tb.text_frame
    tf.word_wrap = True

    p_head = tf.paragraphs[0]
    p_head.text = "CORE PROJECT HIGHLIGHTS & CONTRIBUTIONS"
    p_head.font.name = "Calibri"
    p_head.font.size = Pt(15)
    p_head.font.bold = True
    p_head.font.color.rgb = INDIGO_PRIMARY

    for t in takeaways:
        p = tf.add_paragraph()
        p.text = "✔  " + t
        p.font.name = "Calibri"
        p.font.size = Pt(12.5)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(10)


def render_generic_bullets(slide, bullets):
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True

    for i, b in enumerate(bullets):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = "• " + b
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)


if __name__ == "__main__":
    create_presentation()
