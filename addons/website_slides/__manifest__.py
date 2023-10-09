# -*- coding: utf-8 -*-
{
    'name': 'eLearning',
    'version': '2.7',
    'sequence': 125,
    'summary': 'Manage and publish an eLearning platform',
    'website': 'https://www.odoo.com/app/elearning',
    'category': 'Website/eLearning',
    'description': """
Create Online Courses
=====================

Featuring

 * Integrated course and lesson management
 * Fullscreen navigation
 * Support Youtube videos, Google documents, PDF, images, articles
 * Test knowledge with quizzes
 * Filter and Tag
 * Statistics
""",
    'depends': [
        'portal_rating',
        'website',
        'website_mail',
        'website_profile',
    ],
    'data': [
        'security/website_slides_security.xml',
        'security/ir.model.access.csv',
        'views/gamification_karma_tracking_views.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
        'views/rating_rating_views.xml',
        'views/slide_embed_views.xml',
        'views/slide_question_views.xml',
        'views/slide_slide_partner_views.xml',
        'views/slide_slide_views.xml',
        'views/slide_channel_partner_views.xml',
        'views/slide_channel_views.xml',
        'views/slide_channel_tag_views.xml',
        'views/slide_snippets.xml',
        'views/website_slides_menu_views.xml',
        'views/website_slides_templates_homepage.xml',
        'views/website_slides_templates_course.xml',
        'views/website_slides_templates_lesson.xml',
        'views/website_slides_templates_lesson_fullscreen.xml',
        'views/website_slides_templates_lesson_embed.xml',
        'views/website_slides_templates_profile.xml',
        'views/website_slides_templates_utils.xml',
        'views/website_pages_views.xml',
        'views/slide_channel_add.xml',
        'wizard/slide_channel_invite_views.xml',
        'data/gamification_data.xml',
        'data/mail_activity_type_data.xml',
        'data/mail_message_subtype_data.xml',
        'data/mail_template_data.xml',
        'data/mail_templates.xml',
        'data/slide_data.xml',
        'data/website_data.xml',
    ],
    'demo': [
        'data/res_users_demo.xml',
        'data/slide_channel_tag_demo.xml',
        'data/slide_channel_demo.xml',
        'data/slide_slide_demo.xml',
        'data/slide_user_demo.xml',
        'data/slide_user_gamification_demo.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'website_slides/static/src/activity/**/*',
            'website_slides/static/src/slide_category_one2many_field.js',
            'website_slides/static/src/slide_category_list_renderer.js',
            'website_slides/static/src/scss/slide_views.scss',
            'website_slides/static/src/js/tours/slides_tour.js',
            'website_slides/static/src/js/components/**/*.js',
            'website_slides/static/src/views/**/*.js',
            'website_slides/static/src/views/**/*.xml',
        ],
        'web.assets_frontend': [
            'website_slides/static/src/scss/website_slides.scss',
            'website_slides/static/src/scss/website_slides_profile.scss',
            'website_slides/static/src/scss/slides_slide_fullscreen.scss',
            'website_slides/static/src/js/slides.js',
            'website_slides/static/src/js/slides_share.js',
            'website_slides/static/src/js/slides_upload.js',
            'website_slides/static/src/js/slides_category_add.js',
            'website_slides/static/src/js/slides_category_delete.js',
            'website_slides/static/src/js/slides_slide_archive.js',
            'website_slides/static/src/js/slides_slide_toggle_is_preview.js',
            'website_slides/static/src/js/slides_slide_like.js',
            'website_slides/static/src/js/slides_course_page.js',
            'website_slides/static/src/js/slides_course_slides_list.js',
            'website_slides/static/src/js/slides_course_fullscreen_player.js',
            'website_slides/static/src/js/slides_course_join.js',
            'website_slides/static/src/js/slides_course_enroll_email.js',
            'website_slides/static/src/js/slides_course_prerequisite.js',
            'website_slides/static/src/js/slides_course_quiz.js',
            'website_slides/static/src/js/slides_course_quiz_question_form.js',
            'website_slides/static/src/js/slides_course_quiz_finish.js',
            'website_slides/static/src/js/slides_course_tag_add.js',
            'website_slides/static/src/js/slides_course_unsubscribe.js',
            'website_slides/static/src/js/portal_chatter.js',
            'website_slides/static/src/xml/website_slides_sidebar.xml',
            'website_slides/static/src/xml/website_slides_upload.xml',
            'website_slides/static/src/xml/website_slides_fullscreen.xml',
            'website_slides/static/src/xml/website_slides_share.xml',
            'website_slides/static/src/xml/website_slides_channel_tag.xml',
            'website_slides/static/src/xml/slide_management.xml',
            'website_slides/static/src/xml/slide_course_join.xml',
            'website_slides/static/src/xml/slide_course_prerequisite.xml',
            'website_slides/static/src/xml/slide_quiz_create.xml',
            'website_slides/static/src/xml/slide_quiz.xml',
            'website_slides/static/src/js/public/**/*',
        ],
        'website.assets_editor': [
            'website_slides/static/src/js/systray_items/*.js',
        ],
        'web.assets_tests': [
            'website_slides/static/tests/tours/*.js',
        ],
        'website_slides.slide_embed_assets': [
            # TODO this bundle now includes 'assets_common' files directly, but
            # most of these files are useless in this context, clean this up.
            ('include', 'web._assets_helpers'),

            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',

            'web/static/lib/jquery.ui/jquery-ui.css',
            'web/static/src/libs/fontawesome/css/font-awesome.css',
            'web/static/lib/odoo_ui_icons/*',
            'web/static/lib/select2/select2.css',
            'web/static/lib/select2-bootstrap-css/select2-bootstrap.css',
            'web/static/src/webclient/navbar/navbar.scss',
            'web/static/src/scss/animation.scss',
            'web/static/src/scss/fontawesome_overridden.scss',
            'web/static/src/scss/mimetypes.scss',
            'web/static/src/scss/ui.scss',
            'web/static/src/core/colorpicker/colorpicker.scss',
            'web/static/src/views/fields/translation_dialog.scss',
            'web/static/src/views/fields/signature/signature_field.scss',
            'web/static/src/legacy/scss/ui.scss',
            'web/static/src/legacy/scss/modal.scss',
            'website/static/src/libs/zoomodoo/zoomodoo.scss',

            'web/static/src/legacy/js/promise_extension.js',
            'web/static/src/module_loader.js',
            'web/static/src/session.js',

            'web/static/lib/luxon/luxon.js',
            'web/static/lib/owl/owl.js',
            'web/static/lib/owl/odoo_module.js',
            'web/static/lib/jquery/jquery.js',
            'web/static/lib/jquery.ui/jquery-ui.js',
            'web/static/lib/popper/popper.js',
            'web/static/lib/bootstrap/js/dist/dom/data.js',
            'web/static/lib/bootstrap/js/dist/dom/event-handler.js',
            'web/static/lib/bootstrap/js/dist/dom/manipulator.js',
            'web/static/lib/bootstrap/js/dist/dom/selector-engine.js',
            'web/static/lib/bootstrap/js/dist/base-component.js',
            'web/static/lib/bootstrap/js/dist/alert.js',
            'web/static/lib/bootstrap/js/dist/button.js',
            'web/static/lib/bootstrap/js/dist/carousel.js',
            'web/static/lib/bootstrap/js/dist/collapse.js',
            'web/static/lib/bootstrap/js/dist/dropdown.js',
            'web/static/lib/bootstrap/js/dist/modal.js',
            'web/static/lib/bootstrap/js/dist/offcanvas.js',
            'web/static/lib/bootstrap/js/dist/tooltip.js',
            'web/static/lib/bootstrap/js/dist/popover.js',
            'web/static/lib/bootstrap/js/dist/scrollspy.js',
            'web/static/lib/bootstrap/js/dist/tab.js',
            'web/static/lib/bootstrap/js/dist/toast.js',
            'web/static/lib/select2/select2.js',
            'web/static/lib/clipboard/clipboard.js',
            'web/static/lib/jSignature/jSignatureCustom.js',
            'web/static/src/legacy/js/libs/autocomplete.js',
            'web/static/src/legacy/js/libs/bootstrap.js',
            'web/static/src/legacy/js/libs/jquery.js',
            'website/static/src/libs/zoomodoo/zoomodoo.js',
            'web/static/src/legacy/js/libs/jSignatureCustom.js',
            'web/static/src/legacy/js/core/bus.js',
            'web/static/src/legacy/js/core/class.js',
            'web/static/src/legacy/js/core/dialog.js',
            'web/static/src/legacy/xml/dialog.xml',
            'web/static/src/legacy/js/core/dom.js',
            'web/static/src/legacy/js/core/mixins.js',
            'web/static/src/legacy/js/core/service_mixins.js',
            'web/static/src/legacy/js/core/time.js',
            'web/static/src/legacy/js/core/widget.js',
            'web/static/src/legacy/js/services/core.js',
            'web/static/src/legacy/js/common_env.js',
            'web/static/src/core/**/*.js',
            'web/static/src/env.js',
            'web/static/src/libs/pdfjs.js',
            ('remove', 'web/static/src/core/emoji_picker/emoji_data.js'),

            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap_frontend'),
            'website_slides/static/src/scss/website_slides.scss',
            ('include', 'web.pdf_js_lib'),
            'website_slides/static/lib/pdfslidesviewer/PDFSlidesViewer.js',
            'website_slides/static/src/js/slides_embed.js',
        ],
        'web.tests_assets': [
            'website_slides/static/tests/helpers/*.js',
        ],
        'web.qunit_suite_tests': [
            'website_slides/static/tests/**/*',
            ('remove', 'website_slides/static/tests/tours/**/*'),
            ('remove', 'website_slides/static/tests/helpers/*.js'),
        ],
    },
    'license': 'LGPL-3',
}
