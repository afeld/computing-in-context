[![Columbia SIPA banner](img/sipa.svg)](https://www.sipa.columbia.edu/)

---

# Syllabus

<p style="font-size: 2rem; font-weight:bold; text-align: center;">Computing in Context, Fall 2025</p>

## Course Description

This introductory course will explore computing concepts and coding in the context of solving policy problems. Such problems might include troubleshooting sources of environmental pollution, evaluating the effectiveness of public housing policy or determining the impact that local financial markets have on international healthcare or education. Using policy scenarios as examples, students will be exposed to topics including: requirements gathering, data collection, data cleansing, writing pseudocode and code, using Python packages to help solve policy problems, presenting technical solutions and the constraints of computing. The hands-on nature of the class will help students to develop a strong, transferable skill-set that could be applied to both current coursework and future employment. Between the computer science and policy context lectures, students will see how computer science will become a fundamental component of their policy analysis education.

## Course Information

- **Course Number:** [DSPC6000IA](https://vergil.columbia.edu/vergil/course/20253/105786), formerly INAFU6006
- **Credits:** 3
- **Prerequisites:** none

### Instructors

- **First half:** [Mark Santolucito](https://cs.barnard.edu/profiles/mark-santolucito), msantolu@barnard.edu
- **Second half:** [Aidan Feldman](https://www.sipa.columbia.edu/communities-connections/faculty/aidan-feldman), alf2215@columbia.edu

### Teaching Assistants (TAs)

Section 1:

- Adithi Narayan, an3308@columbia.edu
- Riya Raj, rr3630@columbia.edu

Section 2:

- Shruti Das, sd3875@columbia.edu
- Sneha Palle, sp4434@columbia.edu

## Meeting Information

- All class sessions take place in [IAB](https://maps.app.goo.gl/o1jz3y9X1rT1b8KW7).
- For [DSPC6000IA](https://vergil.columbia.edu/vergil/course/20253/105786), you need to register for the lectures but _don't_ need to register for the labs separately.
  - This isn't clear in Vergil, at time of writing.
- Students should bring a laptop to all labs.
- See [Contexts and Structure](#contexts-and-structure) for more details on how the course is organized.
- [Office hours](office_hours.md)

### Section 1

| Component | Part of term | Start  | End    | Days                   | Times       | Room | Led by           | Contexts  |
| --------- | ------------ | ------ | ------ | ---------------------- | ----------- | ---- | ---------------- | --------- |
| Lecture   | First half   | Sep 2  | Oct 16 | Tuesdays and Thursdays | 1:10-2:25pm | 417  | Mark Santolucito | Combined  |
|           | Second half  | Oct 21 | Dec 4  | Tuesdays and Thursdays | 1:10-2:25pm | 410  | Aidan Feldman    | SIPA only |
| Lab       | Full         | Sep 5  | Dec 5  | Fridays                | 1-2:30pm    | 411  | TAs              | SIPA only |

### Section 2

| Component | Part of term | Start  | End    | Days                   | Times         | Room | Led by           | Contexts  |
| --------- | ------------ | ------ | ------ | ---------------------- | ------------- | ---- | ---------------- | --------- |
| Lecture   | First half   | Sep 2  | Oct 16 | Tuesdays and Thursdays | 1:10-2:25pm   | 417  | Mark Santolucito | Combined  |
|           | Second half  | Oct 21 | Dec 4  | Tuesdays and Thursdays | 3:10–4:25pm\* | 410  | Aidan Feldman    | SIPA only |
| Lab       | Full         | Sep 5  | Dec 5  | Fridays                | 2:40-4:10pm   | 411  | TAs              | SIPA only |

\*Note that the lecture time is different for the second half of the semester.

## Course Overview

### Relationship to Other Courses

- [Comparison with Python for Public Policy](https://python-public-policy.afeld.me/en/columbia/#comparison-to-computing-in-context)
- This is a prerequisite for some [Data Science for Policy (DSP) courses](https://www.sipa.columbia.edu/sipa-education/bulletin/dsp#dsp-requirements), see this [diagram](https://docs.google.com/drawings/d/1PjJG2TdWk-JMU_G2X3BV6ue0N9y5tZUN7FNJ3C8yPX8/edit).

### Contexts and Structure

Computing in Context has multiple sections, each of which correspond to a different "context". Most are listed under the course number [COMS1002W](https://vergil.columbia.edu/vergil/course/20253/37508), SIPA's are [DSPC6000IA](https://vergil.columbia.edu/vergil/course/20253/105786).

The lectures in the first half of the semester have students from multiple contexts, and are taught by Mark Santolucito. The lectures in the second half of the semester are context-specific; SIPA's are taught by Aidan Feldman. The labs (a.k.a. recitations) are context-specific are context-specific the entire semester.

For example, let's say a student is in SIPA (DSPC6000IA) section 1. The first half of the semester, they will attend combined lectures with students from Biology, Linguistics, etc., while doing labs with just their SIPA section. The second half of the semester, they will have both lectures and labs with their SIPA section only.

See also:

- [Meeting Information](#meeting-information)
- [Background on the course](https://www.cs.columbia.edu/2016/computing-in-context-a-computer-science-course-for-liberal-arts-majors-expands-with-new-sipa-track/)

### Testing out

Computing in Context is a required course for [the Data Science for Policy (DSP) concentration and the Data Science for Public Policy minor](https://www.sipa.columbia.edu/sipa-education/bulletin/dsp), and a [prerequisite for various courses](#relationship-to-other-courses). If you have Python+pandas experience, you can test out. The test will:

- Cover the same [topics as the course](#schedule)
- Be 90 minutes (or less)
- Be closed-book

If you pass, you'll be exempt from Computing in Context as a requirement and prerequisite. Instead, you'll choose three credits of other DSP course(s) in its place, and be able to go straight into more advanced classes.

If you _don't_ pass, you'll need to take Computing in Context as normal. Your grade will be unaffected.

To sign up for the test, contact [Aidan](#instructors).

## Grading

See the [combined syllabus][combined-syl] for details. See Gradescope for the assignment rubrics. The final grades for each SIPA section will be [curved](curve.ipynb).

## Schedule

For weeks 1-7, see [the combined syllabus][combined-syl].

| Week | Tuesday                                                                                                            | Thursday                           | Friday                                                                                                                                                        |
| ---- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 8    | **Oct 21**<br/>{doc}`lecture_15`; [new location and instructor](#meeting-information)<hr/>[Lab 7][lab7] due 6pm ET | **Oct 23**<br/>{doc}`lecture_16`   | **Oct 24**<br/>[Reading](week_8.md) due before lab<hr/>[Lab 8: Publishing on the web](lab_8_guide.md)                                                         |
| 9    | **Oct 28**<br/>{doc}`lecture_17`<hr/>[Lab 8](lab_8.ipynb) due 6pm ET                                               | **Oct 30**<br/>{doc}`lecture_18`   | **Oct 31**<br/>[Reading](week_9.md) due before lab<hr/>[Lab 9: Working with data](lab_9_guide.md)                                                             |
| 10   | **Nov 4**<br/>None (Election Day)<hr/>[Lab 9](lab_9.ipynb) due 6pm ET                                              | **Nov 6**<br/>{doc}`lecture_19`    | **Nov 7**<br/>[Reading](week_10.md) due before lab<hr/>[Lab 10: Data cleaning and joining](lab_10_guide.md)<hr/>[Project 1](project_1.md) due 11:59pm ET      |
| 11   | **Nov 11**<br/>{doc}`lecture_20`<hr/>[Lab 10](lab_10.ipynb) due 6pm ET                                             | **Nov 13**<br/>{doc}`lecture_21`   | **Nov 14**<br/>[Reading](week_11.md) due before lab<hr/>[Lab 11: Data visualization](lab_11_guide.md)                                                         |
| 12   | **Nov 18**<br/>{doc}`lecture_22`<hr/>[Lab 11](lab_11.ipynb) due 6pm ET                                             | **Nov 20**<br/>{doc}`lecture_23`   | **Nov 21**<br/>[Reading](week_12.md) due before lab<hr/>[Lab 12: APIs and time series analysis](lab_12_guide.md)<hr/>[Project 2](project_2.md) due 11:59pm ET |
| 13   | **Nov 25**<br/>{doc}`lecture_24` ([virtual][zoom])<hr/>[Lab 12](lab_12.ipynb) due 6pm ET                           | **Nov 27**<br/>None (Thanksgiving) | **Nov 28**<br/>None (Thanksgiving)                                                                                                                            |
| 14   | **Dec 2**<br/>{doc}`lecture_25`                                                                                    | **Dec 4**<br/>[Test](test.md)      | **Dec 5**<br/>Office hours (optional)<hr/>[Project 3](project_3.md) due 11:59pm ET                                                                            |

[lab7]: https://courseworks2.columbia.edu/courses/226977/files/folder/Lab%20Material
[zoom]: https://courseworks2.columbia.edu/courses/230821/external_tools/72338

See also: [Academic Calendar](https://www.registrar.columbia.edu/event/academic-calendar?acfy=49&acterm=6&acschool=18&keys=&field_event_type1_tid%5B%5D=21&field_event_type1_tid%5B%5D=22&field_event_type1_tid%5B%5D=23)

### Generative AI overlap

The [Generative AI course is four Fridays, 10am-5pm](https://vergil.columbia.edu/vergil/course/20253/105790). This overlaps with the [Computing in Context labs](#meeting-information).

The September dates are still in the [first half](#contexts-and-structure), when all contexts are still doing the same material. For students enrolled in both courses, attend one of the [Thursday evening or Friday morning labs](https://vergil.columbia.edu/vergil/course/20253/20303) on those weeks.

The SIPA labs are longer than the other contexts', so SIPA's include more introduction and walkthrough. Students are generally asked to attend the lab for their section — this is an exception.

For the November dates, the labs will be SIPA-specific, so it doesn't make sense to attend labs for the other contexts. Students have [two freebies on the attendance and lab submissions](#grading), so you can use your freebies for the two weeks' labs. Working through the material is still recommended — note the caveats under [Attendance](#attendance).

## Communications

Assignments, due dates, and other aspects of the course may be modified mid-course. As much advance notice will be given as possible.

### Getting help

- Troubleshooting and other communications between class sessions will be through [Ed Discussion][ed].
  - This way, other students can respond and/or benefit from the answers.
  - Don't just say "I got an error." Include the relevant line(s) of code and the full error, copied-and-pasted or as a [screenshot](https://www.take-a-screenshot.org/).
    - See [Academic Integrity policy](#academic-integrity) for guidance on sharing solutions.
- The instructor/TAs will try to respond within 24 hours, 48 hours max, if someone else hasn't already.
- [Office hours](office_hours.md) are also available.
- Email is also an option, though please only use for questions that aren't appropriate for others to see.

## Course Policies

### Wait List

If there ends up being a wait list:

- We expect churn in enrollment, so please be patient.
- One reason for the class size limit is ensuring everyone has a chance to participate. Therefore, it will not be exceeded to accommodate individual students.
- To be fair to everyone, enrollment is first come first served.
- [How the wait list works](https://www.registrar.columbia.edu/content/wait-lists-ssol)
- Worst case, if you don't get in:
  - See the [other Python course options](#relationship-to-other-courses)
  - [There are a lot of other ways to learn Python](https://python-public-policy.afeld.me/en/columbia/resources.html)

### Auditing

See the [school policies](https://www.sipa.columbia.edu/students/student-affairs/academic-advising-faq). Students must be officially [registered](https://bulletin.columbia.edu/sipa/registration/). If there's a wait list, priority for spots in the class will be given to students taking it for credit. Once registered: To receive [R-credit](https://www.registrar.columbia.edu/content/grade-options#auditing), every assignment should at least be attempted and submitted. At the end of the course, please remind the instructor that you were auditing.

### Attendance

See also: [The combined syllabus](https://courseworks2.columbia.edu/courses/226977)

Attending class is mandatory, but most importantly, important. Learning programming requires commitment from the part of the student and the skills are built out of practice. If you miss an experience in class, you miss an important learning moment and the class misses your contribution.

Attendance is only taken for the lab sessions; see below and [grading](#grading) for details. Classes will not be live-streamed or recorded. If you are absent, we trust that it's for a good reason: scheduling conflicts, [religious observance](https://universitypolicies.columbia.edu/content/religious-accommodation-policy), etc. We don't excuse absences beyond that, except in exceptional circumstances. If you're sick, please stay home and rest.

You are responsible for getting caught up on what was covered, without asking the instructors/TAs to re-teach the material to you. You may want to ask a classmate for notes.

#### Labs

See the [combined syllabus][combined-syl].

### Academic Integrity

If you are copying and pasting from a source (see below), it must be cited. This doesn't need to be in a formal style like APA - a comment (and link, where possible) is fine.

**If you did most of the work yourself, it's ok. If most of the work was copied from elsewhere, it's plagiarism,** and will be reported.

#### Sources

Anything outside of the provided course materials is considered a "source". This includes:

- Other students
- Online resources
- Books
- Generative AI (ChatGPT, Claude, Copilot, Gemini, etc.)

#### Other notes

- Students are welcome to work with one another, as long as:
  - You indicate who you worked with
  - The submissions are different
- Students are more than welcome to share approaches and code snippets in the Discussions, so long as they aren't giving the full solution away.
- Students will post the [Projects](https://computing-in-context.afeld.me/projects.html) and [Lab 8](https://computing-in-context.afeld.me/lab_8.html) publicly as part of their [portfolio site](https://computing-in-context.afeld.me/lab_8.html), since they're open-ended. Other assignments (with "correct answers") cannot be posted publicly, to avoid cheating in future semesters. You are more than welcome to share any of your notebooks with specific people, such as future employers.

#### Generative AI

Generative AI tools can be incredibly useful, but the code they provide is often incomplete or wrong. Knowing enough about code to critically interpret their results can turn them from a crutch to a superpower.

For this course, it's recommended that you try doing the work yourself, asking the AI questions as needed when you're stuck/confused. If you're _really_ lost, you can try:

1. Having AI generate a solution.
1. Try it.
   1. Copy it into a code cell.
   1. Run it.
   1. Confirm the output makes sense.
1. Understand it.
   1. Read through it closely.
   1. Add a comment above each line explaining what it's doing.
1. Redo it.
   1. Delete the code + comments from above.
   1. Close the AI chat.
   1. Re-write the solution yourself.

#### SIPA Academic Integrity Statement

The School of International & Public Affairs does not tolerate cheating or plagiarism in any form. Students who violate the Code of Academic & Professional Conduct will be subject to the Dean's Disciplinary Procedures.

Please familiarize yourself with the proper methods of citation and attribution. The School provides some valuable resources online; we strongly encourage you to familiarize yourself with these various styles before conducting research. Cut and paste the following link into your browser to view the Code of Academic & Professional Conduct and to access useful resources on citation and attribution: [https://bulletin.columbia.edu/sipa/academic-policies/](https://bulletin.columbia.edu/sipa/academic-policies/)

Violations of the Code of Academic & Professional Conduct should be reported to the Associate Dean for Student Affairs.

### SIPA Disability Statement

SIPA is committed to ensuring that students registered with [Columbia University's Disability Services](https://health.columbia.edu/content/disability-services) (DS) receive the reasonable accommodations necessary to participate fully in their academic programs. If you are a student with a disability and have a DS-certified accommodation letter, you may wish to make an appointment with your course instructor to discuss your accommodations. Faculty provide disability accommodations to students with DS-certified accommodation letters, and they provide the accommodations specified in such letters. If you have any additional questions, please contact SIPA's DS liaison at disability@sipa.columbia.edu.

<!-- combined -->

<!-- [ed]: https://courseworks2.columbia.edu/courses/226977/external_tools/37606?display=borderless -->

<!-- SIPA -->

[ed]: https://courseworks2.columbia.edu/courses/230821/external_tools/37606?display=borderless

<!-- -------------------------------- -->

[combined-syl]: https://courseworks2.columbia.edu/courses/226977/assignments/syllabus
