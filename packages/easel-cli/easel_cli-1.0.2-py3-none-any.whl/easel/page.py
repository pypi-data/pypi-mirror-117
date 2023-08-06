from tqdm import tqdm

from easel import canvas_id
from easel import component
from easel import course
from easel import helpers

PAGES_PATH=course.COURSE_PATH+"/pages"
PAGE_PATH=PAGES_PATH+"/{}" # page url
TABLE="pages"
WRAPPER="wiki_page"
PAGES_DIR="pages"

class Page(component.Component):

    def __init__(self, url=None, title=None, body=None, published=None,
            front_page=None, todo_date=None, editing_roles=None,
            notify_of_update=None, filename="", student_todo_at=None):
        super().__init__(create_path=PAGES_PATH, update_path=PAGE_PATH,
                db_table=TABLE, canvas_wrapper=WRAPPER, filename=filename)
        self.url = url
        self.title = title
        self.published = published
        self.front_page = front_page
        self.student_todo_at = todo_date
        if student_todo_at:
            self.student_todo_at = student_todo_at
        self.editing_roles = editing_roles
        self.notify_of_update = notify_of_update
        if body:
            self.body = helpers.md2html(body.strip())
        else:
            self.body = body

    def __repr__(self):
        return f"Page(title={self.title}, published={self.published})"

    def preprocess(self, db, course_, dry_run):
        if course_.canvas_id == 741530:
            self.body = self.body.replace("741120", "741530")
            for assign_cid in [{'canvas_id': 9573017, 'course_id': 741120, 'filename': 'assignments/programming_02_-_thonny_installation.yaml'},
                    {'canvas_id': 9573018, 'course_id': 741120, 'filename': 'assignments/programming_03_-_try_codegrinder.yaml'},
                    {'canvas_id': 9573019, 'course_id': 741120, 'filename': 'assignments/programming_06_-_console_i-o.yaml'},
                    {'canvas_id': 9573020, 'course_id': 741120, 'filename': 'assignments/programming_08_-_types.yaml'},
                    {'canvas_id': 9573021, 'course_id': 741120, 'filename': 'assignments/programming_09_-_arithmetic.yaml'},
                    {'canvas_id': 9573022, 'course_id': 741120, 'filename': 'assignments/programming_10_-_conditionals.yaml'},
                    {'canvas_id': 9573023, 'course_id': 741120, 'filename': 'assignments/programming_12_-_variables_and_assignment.yaml'},
                    {'canvas_id': 9573024, 'course_id': 741120, 'filename': 'assignments/programming_13_-_statements_and_expressions.yaml'},
                    {'canvas_id': 9573025, 'course_id': 741120, 'filename': 'assignments/programming_14_-_errors.yaml'},
                    {'canvas_id': 9573026, 'course_id': 741120, 'filename': 'assignments/programming_15_-_strings.yaml'},
                    {'canvas_id': 9573027, 'course_id': 741120, 'filename': 'assignments/programming_16_-_string_operations.yaml'},
                    {'canvas_id': 9573029, 'course_id': 741120, 'filename': 'assignments/programming_17_-_calling_functions.yaml'},
                    {'canvas_id': 9573030, 'course_id': 741120, 'filename': 'assignments/programming_18_-_built-in_functions.yaml'},
                    {'canvas_id': 9573033, 'course_id': 741120, 'filename': 'assignments/programming_20_-_defining_functions.yaml'},
                    {'canvas_id': 9573036, 'course_id': 741120, 'filename': 'assignments/programming_21_-_unit_tests.yaml'},
                    {'canvas_id': 9573039, 'course_id': 741120, 'filename': 'assignments/programming_22_-_return_and_print.yaml'},
                    {'canvas_id': 9573042, 'course_id': 741120, 'filename': 'assignments/programming_23_-_scope.yaml'},
                    {'canvas_id': 9573044, 'course_id': 741120, 'filename': 'assignments/programming_24_-_documenting.yaml'},
                    {'canvas_id': 9573047, 'course_id': 741120, 'filename': 'assignments/programming_27_-_if_statements.yaml'},
                    {'canvas_id': 9573050, 'course_id': 741120, 'filename': 'assignments/programming_29_-_nesting_blocks.yaml'},
                    {'canvas_id': 9573053, 'course_id': 741120, 'filename': 'assignments/programming_30_-_lists.yaml'},
                    {'canvas_id': 9573056, 'course_id': 741120, 'filename': 'assignments/programming_31_-_list_operations.yaml'},
                    {'canvas_id': 9573057, 'course_id': 741120, 'filename': 'assignments/programming_32_-_for_loops.yaml'},
                    {'canvas_id': 9573059, 'course_id': 741120, 'filename': 'assignments/programming_33_-_loop_patterns.yaml'},
                    {'canvas_id': 9573060, 'course_id': 741120, 'filename': 'assignments/programming_34_-_mutability.yaml'},
                    {'canvas_id': 9573064, 'course_id': 741120, 'filename': 'assignments/programming_35_-_lists_vs._strings.yaml'},
                    {'canvas_id': 9573068, 'course_id': 741120, 'filename': 'assignments/programming_37_-_dictionaries.yaml'},
                    {'canvas_id': 9573073, 'course_id': 741120, 'filename': 'assignments/programming_38_-_dictionary_operations.yaml'},
                    {'canvas_id': 9573077, 'course_id': 741120, 'filename': 'assignments/programming_39_-_dictionary_patterns.yaml'},
                    {'canvas_id': 9573082, 'course_id': 741120, 'filename': 'assignments/programming_41_-_nested_data.yaml'},
                    {'canvas_id': 9573086, 'course_id': 741120, 'filename': 'assignments/programming_42_-_while_loops.yaml'},
                    {'canvas_id': 9573091, 'course_id': 741120, 'filename': 'assignments/programming_45_-_files.yaml'},
                    {'canvas_id': 9573095, 'course_id': 741120, 'filename': 'assignments/programming_46_-_modules.yaml'},
                    {'canvas_id': 9573121, 'course_id': 741120, 'filename': 'assignments/test_weights.yaml'},
                    {'canvas_id': 9573100, 'course_id': 741120, 'filename': 'assignments/project_1-_guessing_game.yaml'},
                    {'canvas_id': 9573102, 'course_id': 741120, 'filename': 'assignments/project_2-_turtle_art.yaml'},
                    {'canvas_id': 9573104, 'course_id': 741120, 'filename': 'assignments/project_3-_functional_magic.yaml'},
                    {'canvas_id': 9573110, 'course_id': 741120, 'filename': 'assignments/project_4-_ada_stats.yaml'},
                    {'canvas_id': 9573114, 'course_id': 741120, 'filename': 'assignments/project_5-_text_adventure_game.yaml'},
                    {'canvas_id': 9572997, 'course_id': 741120, 'filename': 'assignments/survey_1-_start_of_course.yaml'},
                    {'canvas_id': 9573008, 'course_id': 741120, 'filename': 'assignments/critique_1-_names.yaml'},
                    {'canvas_id': 9573009, 'course_id': 741120, 'filename': 'assignments/critique_2-_documentation.yaml'},
                    {'canvas_id': 9573010, 'course_id': 741120, 'filename': 'assignments/field_work_-_data_collection.yaml'},
                    {'canvas_id': 9573015, 'course_id': 741120, 'filename': 'assignments/play_a_game.yaml'},
                    {'canvas_id': 9573012, 'course_id': 741120, 'filename': 'assignments/make_a_game_plan.yaml'},
                    {'canvas_id': 9572980, 'course_id': 741120, 'filename': 'assignments/final_survey.yaml'},
                    {'canvas_id': 9573119, 'course_id': 741120, 'filename': 'assignments/roll_call_attendance.yaml'},
                    {'canvas_id': 9573013, 'course_id': 741120, 'filename': 'assignments/midterm_1-_part_2.yaml'},
                    {'canvas_id': 9573014, 'course_id': 741120, 'filename': 'assignments/midterm_2-_part_2.yaml'},
                    {'canvas_id': 9573011, 'course_id': 741120, 'filename': 'assignments/final_exam-_part_2.yaml'},
                    {'canvas_id': 9573016, 'course_id': 741120, 'filename': 'assignments/programming_01_-_maze_game.yaml'},
                    {'canvas_id': 2344382, 'course_id': 741120, 'filename': 'quizzes/quiz_10-_conditionals.yaml'},
                    {'canvas_id': 2344419, 'course_id': 741120, 'filename': 'quizzes/quiz_11-_variables.yaml'},
                    {'canvas_id': 2344413, 'course_id': 741120, 'filename': 'quizzes/quiz_12-_tracing.yaml'},
                    {'canvas_id': 2344376, 'course_id': 741120, 'filename': 'quizzes/quiz_13-_statements_and_expressions.yaml'},
                    {'canvas_id': 2344403, 'course_id': 741120, 'filename': 'quizzes/quiz_14-_errors.yaml'},
                    {'canvas_id': 2344383, 'course_id': 741120, 'filename': 'quizzes/quiz_15-_strings.yaml'},
                    {'canvas_id': 2344379, 'course_id': 741120, 'filename': 'quizzes/quiz_16-_string_operations.yaml'},
                    {'canvas_id': 2344401, 'course_id': 741120, 'filename': 'quizzes/quiz_17-_calling_functions.yaml'},
                    {'canvas_id': 2344390, 'course_id': 741120, 'filename': 'quizzes/quiz_18-_calling_functions_2.yaml'},
                    {'canvas_id': 2344415, 'course_id': 741120, 'filename': 'quizzes/quiz_19-_debugging.yaml'},
                    {'canvas_id': 2344371, 'course_id': 741120, 'filename': 'quizzes/quiz_1_-_introduction.yaml'},
                    {'canvas_id': 2344409, 'course_id': 741120, 'filename': 'quizzes/quiz_20-_defining_functions.yaml'},
                    {'canvas_id': 2344387, 'course_id': 741120, 'filename': 'quizzes/quiz_21-_unit_tests.yaml'},
                    {'canvas_id': 2344370, 'course_id': 741120, 'filename': 'quizzes/quiz_22-_return_and_print.yaml'},
                    {'canvas_id': 2344408, 'course_id': 741120, 'filename': 'quizzes/quiz_23-_scope.yaml'},
                    {'canvas_id': 2344386, 'course_id': 741120, 'filename': 'quizzes/quiz_24-_documenting.yaml'},
                    {'canvas_id': 2344395, 'course_id': 741120, 'filename': 'quizzes/quiz_25-_functional_decomposition.yaml'},
                    {'canvas_id': 2344391, 'course_id': 741120, 'filename': 'quizzes/quiz_26-_data_flow.yaml'},
                    {'canvas_id': 2344418, 'course_id': 741120, 'filename': 'quizzes/quiz_27-_if_statements.yaml'},
                    {'canvas_id': 2344398, 'course_id': 741120, 'filename': 'quizzes/quiz_28-_truthiness.yaml'},
                    {'canvas_id': 2344417, 'course_id': 741120, 'filename': 'quizzes/quiz_29-_nesting_blocks.yaml'},
                    {'canvas_id': 2344377, 'course_id': 741120, 'filename': 'quizzes/quiz_2-_language.yaml'},
                    {'canvas_id': 2344373, 'course_id': 741120, 'filename': 'quizzes/quiz_30-_lists.yaml'},
                    {'canvas_id': 2344394, 'course_id': 741120, 'filename': 'quizzes/quiz_31-_list_operations.yaml'},
                    {'canvas_id': 2344406, 'course_id': 741120, 'filename': 'quizzes/quiz_32-_for_loops.yaml'},
                    {'canvas_id': 2344416, 'course_id': 741120, 'filename': 'quizzes/quiz_33-_loop_patterns.yaml'},
                    {'canvas_id': 2344420, 'course_id': 741120, 'filename': 'quizzes/quiz_34-_mutability.yaml'},
                    {'canvas_id': 2344407, 'course_id': 741120, 'filename': 'quizzes/quiz_35-_lists_and_strings.yaml'},
                    {'canvas_id': 2344384, 'course_id': 741120, 'filename': 'quizzes/quiz_36-_lists_and_indexes.yaml'},
                    {'canvas_id': 2344385, 'course_id': 741120, 'filename': 'quizzes/quiz_37-_dictionaries.yaml'},
                    {'canvas_id': 2344388, 'course_id': 741120, 'filename': 'quizzes/quiz_38-_dictionary_operations.yaml'},
                    {'canvas_id': 2344393, 'course_id': 741120, 'filename': 'quizzes/quiz_39-_dictionary_patterns.yaml'},
                    {'canvas_id': 2344380, 'course_id': 741120, 'filename': 'quizzes/quiz_3-_execution.yaml'},
                    {'canvas_id': 2344402, 'course_id': 741120, 'filename': 'quizzes/quiz_40-_lookup_and_find.yaml'},
                    {'canvas_id': 2344404, 'course_id': 741120, 'filename': 'quizzes/quiz_41-_nested_data.yaml'},
                    {'canvas_id': 2344389, 'course_id': 741120, 'filename': 'quizzes/quiz_42-_while_loops.yaml'},
                    {'canvas_id': 2344412, 'course_id': 741120, 'filename': 'quizzes/quiz_45-_files.yaml'},
                    {'canvas_id': 2344399, 'course_id': 741120, 'filename': 'quizzes/quiz_46-_modules.yaml'},
                    {'canvas_id': 2344375, 'course_id': 741120, 'filename': 'quizzes/quiz_4-_learning.yaml'},
                    {'canvas_id': 2344381, 'course_id': 741120, 'filename': 'quizzes/quiz_5-_getting_help.yaml'},
                    {'canvas_id': 2344397, 'course_id': 741120, 'filename': 'quizzes/quiz_6-_console_io.yaml'},
                    {'canvas_id': 2344414, 'course_id': 741120, 'filename': 'quizzes/quiz_7-_values.yaml'},
                    {'canvas_id': 2344369, 'course_id': 741120, 'filename': 'quizzes/quiz_8-_types.yaml'},
                    {'canvas_id': 2344405, 'course_id': 741120, 'filename': 'quizzes/quiz_9-_arithmetic.yaml'}]:
                # find cid for assign_cid
                cid = canvas_id.CanvasID(assign_cid['filename'], course_.canvas_id)
                cid.find_id(db)
                prefix = assign_cid['filename'].split('/')[0]
                fname = assign_cid['filename'].split('/')[1]
                self.body = self.body.replace(f"assignments/{assign_cid['canvas_id']}", f"assignments/{cid.canvas_id}")
                if prefix == "quizzes":
                    qi = self.body.find("Quiz")
                    if qi == -1:
                        continue
                    part1 = self.body[:qi]
                    part2 = self.body[qi:]
                    url = "<" + part1.split('<')[-1]
                    if "quizzes" in url:
                        continue
                    text = part2.split("<")[0]
                    quiznum = str(int(text.split('-')[0][5:]))
                    quizprefix = fname.split('_')[0]
                    fnamepart = fname.split('_')[1]
                    if quizprefix == "quiz" and ((quiznum == '1' and fname == 'quiz_1_-_introduction.yaml') or quiznum == fnamepart[:fnamepart.find('-')]):
                        cid = canvas_id.CanvasID(assign_cid['filename'], course_.canvas_id)
                        cid.find_id(db)
                        quizid = cid.canvas_id
                        urlparts = url.split("assignments")
                        urlparts[1] = f"/{quizid}\" "+ '"'.join(urlparts[1].split('"')[1:])
                        urlparts[2] = f"/{quizid}\" "+ '"'.join(urlparts[2].split('"')[1:])
                        newurl = "quizzes".join(urlparts)
                        print(url)
                        print(newurl)
                        self.body = self.body.replace(url, newurl)


    @classmethod
    def build(cls, fields):
        extras = ['page_id', 'created_at', 'updated_at',
                'hide_from_students', 'last_edited_by', 'locked_for_user',
                'lock_info', 'lock_explanation', 'html_url']
        defaults = [("front_page", False),
                ("editing_roles", "teachers")]
        component.filter_fields(fields, extras, defaults)
        if 'body' in fields:
            fields['body'] = helpers.filter_canvas_html(fields['body'])
        return Page(**fields)

# Needed for custom yaml tag
def constructor(loader, node):
    return Page(**loader.construct_mapping(node))

def pull_page(db, course_id, page_url, dry_run):
    page_ = helpers.get(PAGE_PATH.format(course_id, page_url), dry_run=dry_run)
    cid = canvas_id.find_by_id(db, course_id, page_.get('url'))
    if cid:
        page_['filename'] = cid.filename
    else:
        page_['filename'] = component.gen_filename(PAGES_DIR, page_.get('title', ''))
        cid = canvas_id.CanvasID(page_['filename'], course_id)
        cid.canvas_id = page_.get('url')
        cid.save(db)
    return Page.build(page_), cid

def pull_all(db, course_, dry_run):
    r = helpers.get(PAGES_PATH.format(course_.canvas_id),
            dry_run=dry_run)
    pages = []
    print("pulling page contents")
    for p in tqdm(r):
        page_, _ = pull_page(db, course_.canvas_id, p.get('url'), dry_run)
        pages.append(page_)
    return pages
