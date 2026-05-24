#!/usr/bin/env python3
"""
create_allotta_naut_game_one_plot_notes.py

Drop this file into the root of your AllottaNaut Obsidian vault or run it from anywhere
with --root pointing at your vault.

It creates an Obsidian-ready story spine for AllottaNaut Game One, including:
- A main plot discussion / book spine note
- Individual chapter notes
- Supporting notes for mechanics-as-story, themes, and open questions

Default behavior is safe: it will NOT overwrite existing notes unless --overwrite is used.

Examples:
    python create_allotta_naut_game_one_plot_notes.py
    python create_allotta_naut_game_one_plot_notes.py --root "C:/Users/admin/Documents/GitHub/AllottaNaut-Obsidian-vault"
    python create_allotta_naut_game_one_plot_notes.py --overwrite
    python create_allotta_naut_game_one_plot_notes.py --dry-run
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Iterable


PROJECT_DIR = Path("AllottaNaut")
GAME_ONE_DIR = PROJECT_DIR / "Game One"
PLOT_DIR = GAME_ONE_DIR / "Plot"
CHAPTER_DIR = PLOT_DIR / "Chapters"
SUPPORT_DIR = PLOT_DIR / "Support Notes"


@dataclass(frozen=True)
class Note:
    relative_path: Path
    content: str


def frontmatter(
    title: str,
    entry_type: str = "plot_note",
    status: str = "draft",
    focus: str = "AllottaNaut Game One",
    tags: Iterable[str] | None = None,
) -> str:
    tag_lines = "\n".join(f"  - {tag}" for tag in (tags or []))
    return dedent(
        f"""\
        ---
        title: {title}
        project: AllottaNaut
        game: Game One
        entry_type: {entry_type}
        status: {status}
        focus: {focus}
        tags:
        {tag_lines}
        ---

        """
    )


def md_link(title: str) -> str:
    return f"[[{title}]]"


def main_spine_note() -> Note:
    title = "Game One - Plot Discussion - Book Spine"
    chapter_titles = [
        "Game One - Prologue - The Survey Before the Impossible",
        "Game One - Chapter 1 - The Breach",
        "Game One - Chapter 2 - Floating Lessons",
        "Game One - Chapter 3 - The First Anchor",
        "Game One - Chapter 4 - The Place Imitates",
        "Game One - Chapter 5 - The First Ground",
        "Game One - Chapter 6 - Brother Contrast",
        "Game One - Chapter 7 - The Memory Garden",
        "Game One - Chapter 8 - The False Help",
        "Game One - Chapter 9 - Nodes Beyond the Self",
        "Game One - Chapter 10 - Gravity Pockets",
        "Game One - Chapter 11 - The First Question",
        "Game One - Chapter 12 - The Cost of Teaching",
        "Game One - Chapter 13 - The Boundary Lesson",
        "Game One - Chapter 14 - The Door Back",
        "Game One - Chapter 15 - Expulsion",
        "Game One - Epilogue - First Light",
    ]

    chapter_links = "\n".join(f"{idx + 1}. {md_link(chapter)}" for idx, chapter in enumerate(chapter_titles))

    content = frontmatter(
        title=title,
        entry_type="plot_discussion",
        focus="Intro-to-ending story spine",
        tags=["AllottaNaut", "Game-One", "Plot", "Story-Spine", "Obsidian"],
    ) + dedent(
        f"""\
        # {title}

        ## Purpose

        This note treats **AllottaNaut Game One** like a short book: a sequence of chapters,
        scenes, emotional turns, gameplay lessons, and worldbuilding reveals.

        The goal is not to lock the exact script yet. The goal is to create a clean story spine
        that can later become scene notes, dialogue drafts, level designs, quest beats, and
        implementation tasks.

        Game One should feel small enough to finish, but emotionally large enough to prove what
        AllottaNaut is.

        > Two brothers enter a place that should not exist, meet a reality that does not
        > understand itself, and accidentally become the first people to teach it how to be.

        ---

        ## Working Premise

        Elias and Rowen are scouts/surveyors from an advanced Type II civilization. Their society
        is organized, council-driven, educated, and capable of enormous engineering projects,
        including a Dyson sphere-style energy network.

        During a mission, they encounter an impossible anomaly: not a planet, not a star, not a
        wormhole, not a normal pocket dimension, but a living reality in its earliest state.

        This reality is **AllottaNaut**.

        At the start, AllottaNaut is almost empty. It has no stable rules, no true ground, no sky,
        no gravity, no weather, no history, no ecology, and no cultural meaning. It has a seed-like
        center, and around it is a void that is not dead but unborn.

        Elias and Rowen do not immediately understand that they are inside something alive.
        AllottaNaut does not immediately understand that they are alive either.

        The game becomes a first conversation between people and a reality.

        ---

        ## Main Emotional Throughline

        ### Elias

        Elias begins with control. He is calculated, sharp, authoritative, and mechanically
        philosophical. His first instinct is to classify, measure, stabilize, and protect.

        His arc is learning that not every unknown thing is a machine waiting to be solved.
        Some things are children. Some things are lonely. Some things are listening before they
        know what listening means.

        By the end of Game One, Elias understands that being precise also means being careful
        with what you teach a newborn reality.

        ### Rowen

        Rowen begins with presence. He is physically stronger, expressive, thoughtful, and more
        emotionally philosophical. He trusts his gut and his empathy faster than Elias does.

        His arc is learning that compassion also carries consequences. If AllottaNaut imitates
        everything it feels from them, then comfort, fear, anger, grief, play, and curiosity can
        all become architecture.

        By the end of Game One, Rowen understands that kindness is not just warmth. It is also
        responsibility.

        ### AllottaNaut

        AllottaNaut begins without language, without form, and without self-awareness in the
        human sense. It exists, but it does not know what existing means.

        It learns through contact.

        It does not create because it has a plan. It creates because something enters it, moves
        through it, fears inside it, laughs inside it, touches it, names it, and asks it to respond.

        AllottaNaut's arc is the birth of intentionality.

        At first it reacts. Then it imitates. Then it associates. Then it anticipates. Then it chooses.

        ---

        ## Chapter List

        {chapter_links}

        ---

        ## Supporting Notes

        - [[Game One - Mechanics as Story Lessons]]
        - [[Game One - Major Themes]]
        - [[Game One - Current Best Ending Shape]]
        - [[Game One - Development Scope Notes]]
        - [[Game One - Working Questions]]

        ---

        ## One-Sentence Player Promise

        > You play as two explorer brothers floating through a newborn living reality. As you move,
        > talk, and solve puzzles, the world learns from you and slowly invents gravity, ground,
        > memory, and boundaries.

        ---

        ## Current Strongest Spine

        Elias and Rowen do not just explore AllottaNaut. They accidentally become the first beings
        to teach it motion, attention, support, memory, consequence, boundary, and letting go.

        The cleanest ending for Game One is not AllottaNaut becoming powerful. It is AllottaNaut
        becoming aware enough to choose restraint.

        > AllottaNaut wants to keep Elias and Rowen, but because they taught it care and boundary,
        > it lets them go.
        """
    )

    return Note(PLOT_DIR / f"{title}.md", content)


def chapter_note(
    title: str,
    story_function: str,
    scene_summary: str,
    emotional_tone: str,
    gameplay_purpose: str,
    allotta_naut_learning: str,
    next_note: str | None = None,
    previous_note: str | None = None,
) -> Note:
    nav_lines = []
    if previous_note:
        nav_lines.append(f"- Previous: [[{previous_note}]]")
    nav_lines.append("- Spine: [[Game One - Plot Discussion - Book Spine]]")
    if next_note:
        nav_lines.append(f"- Next: [[{next_note}]]")

    navigation = "\n".join(nav_lines)

    content = frontmatter(
        title=title,
        entry_type="chapter_note",
        focus=title,
        tags=["AllottaNaut", "Game-One", "Plot", "Chapter"],
    ) + dedent(
        f"""\
        # {title}

        ## Navigation

        {navigation}

        ---

        ## Story Function

        {story_function}

        ---

        ## Scene Summary

        {scene_summary}

        ---

        ## Emotional Tone

        {emotional_tone}

        ---

        ## Gameplay Purpose

        {gameplay_purpose}

        ---

        ## AllottaNaut's Learning Beat

        {allotta_naut_learning}

        ---

        ## Dialogue Seeds

        - Elias should express the pressure to classify, stabilize, and protect.
        - Rowen should express presence, empathy, curiosity, and concern.
        - Their bond should show through shorthand instead of exposition.

        ---

        ## Implementation Notes

        - Keep the scene small enough to prototype.
        - Tie at least one player action directly to the story lesson.
        - Avoid overexplaining AllottaNaut too early.
        - Let the environment communicate before full dialogue does.

        ---

        ## Expansion To-Do

        - [ ] Add beat-by-beat scene outline.
        - [ ] Add first draft dialogue.
        - [ ] Add required assets.
        - [ ] Add required mechanics.
        - [ ] Add Godot implementation notes.
        """
    )

    return Note(CHAPTER_DIR / f"{title}.md", content)


def chapter_notes() -> list[Note]:
    chapters = [
        (
            "Game One - Prologue - The Survey Before the Impossible",
            "Ground Elias and Rowen before the player sees the void. The player should understand that these brothers come from somewhere real, structured, and lived-in.",
            "The game opens aboard a survey craft, observation station, or small scouting vessel near the edge of a known survey zone. Elias and Rowen are working a routine anomaly scan. The anomaly does not behave like mass, radiation, dark matter, a gravity well, or a standard spatial tear. It is not pulling them in exactly. It is almost noticing them.",
            "Quiet, professional, slightly tired, brotherly, then wrong.",
            "Minimal control or no control. This can be cinematic, a walking section, or a small interaction space. The player learns that Elias and Rowen are trained, that the outside universe has rules, and that the anomaly breaks those rules.",
            "None yet, or only the faintest first contact. AllottaNaut is simply present.",
        ),
        (
            "Game One - Chapter 1 - The Breach",
            "Cross the threshold from the known universe into the unmade place.",
            "The anomaly opens or folds around them. Ship systems fail in ways that do not make mechanical sense. Instead of explosion or destruction, the environment becomes less defined. Sound drops out. Gravity loses meaning. Their instruments either go blank, loop impossible values, or begin displaying data that was never programmed into them.",
            "Awe mixed with dread. Not gore-horror, but the feeling of being watched by a place that does not yet know what watching is.",
            "Title transition and first movement handoff. The player should feel that the old rules are gone, the brothers survived, and there is no stable down.",
            "AllottaNaut encounters living minds inside itself. It does not understand them yet.",
        ),
        (
            "Game One - Chapter 2 - Floating Lessons",
            "Introduce the true gameplay opening: floating through a void with no stable rules.",
            "Elias and Rowen regain awareness in the void. Their suits are intact enough to communicate, but their readings are unreliable. There is no floor. They drift. The player learns the float mechanic: gentle movement, uncertain steering, and pulse movement through unborn space.",
            "Disorientation, beauty, fragile humor, brotherly tension.",
            "Teach floating movement, pulse/burst movement, camera orientation, following or reuniting with the other brother, and interacting with simple glowing objects.",
            "AllottaNaut learns motion. It observes that Elias and Rowen move with intention.",
        ),
        (
            "Game One - Chapter 3 - The First Anchor",
            "Give the player a goal in the void and give AllottaNaut its first object of shared meaning.",
            "In the distance, Elias detects a fixed point. Rowen sees it more like a light or center. It may be the Seed, Naut, or the first visible singularity. The brothers move toward it while the void subtly organizes around their approach.",
            "Curiosity begins to overtake panic.",
            "Teach reaching a target, interacting with the seed/anchor, simple cause and effect, and environmental response.",
            "AllottaNaut learns attention. It learns that the brothers look toward things, move toward things, and treat some things as important.",
        ),
        (
            "Game One - Chapter 4 - The Place Imitates",
            "Reveal AllottaNaut's central magic: it learns by imitation.",
            "After interacting with the first anchor, the void begins producing spaces that resemble things Elias and Rowen reference, remember, or emotionally project. At first the imitations are basic: a floor that is only a flat thought, a wall that exists because Elias says they need boundaries, a door that leads nowhere until Rowen asks where it goes.",
            "Wonder, concern, philosophical friction.",
            "Teach environmental puzzles, interacting with formed objects, using movement to trigger formation, and possibly collecting or activating nodes.",
            "AllottaNaut learns imitation. It begins to copy movement, light, structure, emotional emphasis, and spoken concepts.",
        ),
        (
            "Game One - Chapter 5 - The First Ground",
            "Transition from pure floating into the first walking section. This should feel like a major emotional and mechanical milestone.",
            "The brothers reach a denser region of formed space. Particles gather beneath them. Their drifting slows. A surface appears, unstable at first, then steady enough for boots. The first time they stand should matter.",
            "Relief, awe, and a little sadness, because the first stable ground feels like a gift from something that does not know why they needed it.",
            "Introduce walking movement, jumping or stepping, basic precision traversal, camera logic around grounded movement, and interaction with stable objects.",
            "AllottaNaut learns support. It observes that the brothers struggle without anchor points and feel safer when standing.",
        ),
        (
            "Game One - Chapter 6 - Brother Contrast",
            "Let the brothers stop surviving long enough to disagree. Deepen Elias and Rowen while clarifying the ethical problem.",
            "Elias wants strict control: no unnecessary speech, no emotional projection, no speculation aloud, no touching unknown structures unless tested. Rowen pushes back, arguing that they cannot treat this place like a dead hazard if it keeps responding like something alive.",
            "Tension, love, fear disguised as irritation.",
            "Use a puzzle where Elias's analysis reveals structure and Rowen's empathy reveals response. Neither alone solves the path forward.",
            "AllottaNaut learns conflict. It may copy disagreement as environmental division: colder angular structures near Elias, warmer flowing structures near Rowen, split paths, and objects that only form through cooperation.",
        ),
        (
            "Game One - Chapter 7 - The Memory Garden",
            "Move AllottaNaut from abstract imitation to emotionally meaningful creation.",
            "The brothers enter a formed region that resembles a garden, shoreline, childhood place, training field, family room, or blended memory from both brothers. It is not a perfect flashback. It is a dreamlike reconstruction built from emotional residue.",
            "Melancholy wonder. Home seen through a stranger's eyes.",
            "Introduce gentle exploration, environmental storytelling, optional dialogue triggers, memory fragments, and non-combat puzzle flow.",
            "AllottaNaut learns memory. Not factual memory, but emotional memory. It learns that places can mean things.",
        ),
        (
            "Game One - Chapter 8 - The False Help",
            "Show that AllottaNaut can be innocent and still dangerous.",
            "AllottaNaut tries to help based on incomplete understanding. It may create too much gravity, fold space painfully, copy fear into threat-shapes, create a home that traps them, or imitate the ship with impossible wrongness.",
            "Stress, confusion, sympathy. The player should feel that AllottaNaut is not evil. It is powerful and untrained.",
            "Introduce hazard avoidance, unstable gravity or movement shifts, calming/stabilizing nodes, and possible timed escape without turning the game into combat.",
            "AllottaNaut learns mistake. This may be the first time it changes behavior after causing harm.",
        ),
        (
            "Game One - Chapter 9 - Nodes Beyond the Self",
            "Reveal that AllottaNaut is not only a contained place. It has nodes or tendrils that reach outward beyond itself.",
            "The brothers discover node-like structures extending from the seed/core into impossible directions. These nodes may be how AllottaNaut senses other realities, universes, thoughts, or spaces. It does not fully control where the nodes go yet.",
            "Cosmic scale with intimate motive. Like seeing a baby reach toward a power outlet, except the baby is a reality.",
            "Introduce node activation, path linking, glimpses of other possible worlds, and navigation between formed pockets.",
            "AllottaNaut learns outside. Until now, everything was inside. This is the first idea that there are other places and beings beyond itself.",
        ),
        (
            "Game One - Chapter 10 - Gravity Pockets",
            "Develop the Mario Galaxy-inspired local gravity idea in AllottaNaut's own language.",
            "The brothers enter a region of scattered small bodies. Each one has its own local gravity. Some are tiny planets. Some are cubes, rings, broken shells, or symbolic objects. Floating returns between them, while walking becomes precise once a gravity pocket catches them.",
            "Playful wonder with underlying danger.",
            "Introduce local gravity zones, floating-to-walking transitions, surface traversal, small-world puzzle design, and optional collectibles/dialogue memories.",
            "AllottaNaut learns world-shape. It begins to understand that worlds are relationships between gravity, movement, horizon, path, and purpose.",
        ),
        (
            "Game One - Chapter 11 - The First Question",
            "Let AllottaNaut attempt communication without suddenly becoming fluent.",
            "After enough interaction, AllottaNaut creates a repeated pattern: light pulses, object arrangements, mirrored movements, sound fragments, or images. Elias realizes it is not random. Rowen realizes it is asking something.",
            "Reverent and quiet. The moment the anomaly becomes a person-like presence.",
            "Introduce a response mechanic through action rather than a normal dialogue menu: standing near lights, activating symbols, moving together or apart, or offering an object/memory.",
            "AllottaNaut learns question. It no longer only reacts. It seeks information.",
        ),
        (
            "Game One - Chapter 12 - The Cost of Teaching",
            "Make the brothers realize that every interaction has shaped AllottaNaut.",
            "AllottaNaut begins combining lessons: motion, attention, support, imitation, memory, conflict, outside, and question. The result is unstable. Elias and Rowen realize they are not neutral observers.",
            "Heavy, responsible, not hopeless.",
            "Escalate the mid-to-late game with a larger puzzle chain, revisiting earlier mechanics in combined form, stabilizing multiple nodes, and using both float and walk/gravity movement.",
            "AllottaNaut learns consequence. It begins to understand that what it does affects others.",
        ),
        (
            "Game One - Chapter 13 - The Boundary Lesson",
            "Teach AllottaNaut not just how to create, but how to stop.",
            "A node begins reaching too far, possibly toward Elias and Rowen's home reality or another unknown place. AllottaNaut does not understand that contact can become intrusion. The brothers cannot destroy the node without hurting AllottaNaut. They must guide it into a boundary.",
            "Tender, tense, formative. Not a boss fight. More like teaching a god-child not to squeeze the bird it loves.",
            "Climax mechanic: stabilize a node, alternate between floating and grounded gravity pockets, use Elias/Rowen cooperation, and trigger responses based on positioning, rhythm, or interaction order.",
            "AllottaNaut learns boundary. This prevents AllottaNaut from becoming a cheap omnipotent force and gives the concept ethics, tension, and story rules.",
        ),
        (
            "Game One - Chapter 14 - The Door Back",
            "Have AllottaNaut respond to the boundary lesson by creating a way for Elias and Rowen to leave.",
            "A path forms. It may resemble the original anomaly, their ship, a doorway, a horizon, or a small opening in the void. Elias wants to take the chance while it exists. Rowen hesitates because leaving feels like abandoning a child.",
            "Bittersweet, quiet, restrained.",
            "Final reflective traversal through memories of mechanics. Low difficulty, reflective dialogue, optional final interactions.",
            "AllottaNaut learns letting go. This completes the emotional lesson of boundary.",
        ),
        (
            "Game One - Chapter 15 - Expulsion",
            "Return the brothers changed and set up future games.",
            "Elias and Rowen are expelled, released, or returned to normal space. Their ship may be damaged, missing time, relocated, or impossible to explain. Their society may read the event as disaster, miracle, contamination, or security threat.",
            "Aftershock, awe, unfinished business.",
            "Ending cinematic or short controllable epilogue. Possible actions: walk through damaged ship, respond to transmissions, see a faint AllottaNaut signal, or choose what to report.",
            "AllottaNaut learns absence. The brothers are gone, but their lessons remain.",
        ),
        (
            "Game One - Epilogue - First Light",
            "Land the meaning of First Light: not just visible light, but AllottaNaut's first inner light.",
            "Back inside AllottaNaut, the void is no longer completely empty. A small surface remains. A light pulses. A node retracts instead of reaching too far. Another node gently opens, not as invasion, but as curiosity.",
            "Quiet, enormous, hopeful.",
            "A final non-playable or lightly playable beat showing the world after Elias and Rowen leave.",
            "AllottaNaut begins to form identity. The clean final signal may be: I am here.",
        ),
    ]

    notes: list[Note] = []
    titles = [item[0] for item in chapters]

    for index, chapter in enumerate(chapters):
        title, story_function, scene_summary, emotional_tone, gameplay_purpose, learning = chapter
        previous_note = titles[index - 1] if index > 0 else None
        next_note = titles[index + 1] if index + 1 < len(titles) else None
        notes.append(
            chapter_note(
                title=title,
                story_function=story_function,
                scene_summary=scene_summary,
                emotional_tone=emotional_tone,
                gameplay_purpose=gameplay_purpose,
                allotta_naut_learning=learning,
                previous_note=previous_note,
                next_note=next_note,
            )
        )

    return notes


def support_notes() -> list[Note]:
    mechanics_content = frontmatter(
        "Game One - Mechanics as Story Lessons",
        entry_type="support_note",
        focus="Mechanics tied to AllottaNaut learning stages",
        tags=["AllottaNaut", "Game-One", "Mechanics", "Story"],
    ) + dedent(
        """\
        # Game One - Mechanics as Story Lessons

        | Mechanic | Story Meaning | AllottaNaut Learns |
        |---|---|---|
        | Floating | No stable reality yet | Motion |
        | Pulse/Burst Movement | Intention creates direction | Intent |
        | First Anchor/Seed | Something matters because it is attended to | Attention |
        | Object Interaction | Cause and effect | Response |
        | Formed Platforms | Need creates structure | Support |
        | Walking | Reality stabilizes around bodies | Down / Ground |
        | Gravity Pockets | Worlds are local rule systems | World-shape |
        | Environmental Puzzles | Meaning can be arranged | Relationship |
        | Memory Spaces | Places can carry feeling | Memory |
        | Node Stabilization | Reaching must have limits | Boundary |
        | Final Door | Love does not mean possession | Letting go |

        ## Design Principle

        Every major mechanic should also be a lesson AllottaNaut learns.

        The player should never feel like the story pauses so gameplay can happen.
        The gameplay is the method of teaching the world.
        """
    )

    themes_content = frontmatter(
        "Game One - Major Themes",
        entry_type="support_note",
        focus="Themes",
        tags=["AllottaNaut", "Game-One", "Themes"],
    ) + dedent(
        """\
        # Game One - Major Themes

        ## Creation Through Relationship

        AllottaNaut does not become a world alone. It becomes a world because someone enters,
        reacts, names, fears, loves, and teaches.

        ## Power Needs Boundaries

        AllottaNaut's potential is nearly unlimited, but Game One should immediately establish
        that potential without restraint is dangerous.

        The most important early lesson is not power. It is care.

        ## Brothers as Two Forms of Responsibility

        Elias and Rowen should not be reduced to simple logic versus emotion.

        - Elias: responsibility through structure, caution, analysis, and control.
        - Rowen: responsibility through empathy, presence, trust, and care.

        AllottaNaut needs both.

        ## The Cosmic Made Intimate

        The game can involve reality-bending concepts, but the player should experience them
        through small actions:

        - standing for the first time
        - reaching a light
        - calming a mistake
        - answering a question
        - leaving someone who just learned connection
        """
    )

    ending_content = frontmatter(
        "Game One - Current Best Ending Shape",
        entry_type="support_note",
        focus="Ending",
        tags=["AllottaNaut", "Game-One", "Ending"],
    ) + dedent(
        """\
        # Game One - Current Best Ending Shape

        The cleanest ending for Game One is not AllottaNaut becoming powerful.

        It is AllottaNaut becoming aware enough to choose restraint.

        > AllottaNaut wants to keep Elias and Rowen, but because they taught it care and boundary,
        > it lets them go.

        That ending does three things at once:

        1. It proves AllottaNaut is alive.
        2. It proves Elias and Rowen changed it.
        3. It proves the story has rules, so future reality-bending does not feel cheap.

        ## Possible Final Signal

        The cleanest final line or signal may be:

        > I am here.

        This should feel enormous because AllottaNaut began as a reality that existed without
        knowing what existence meant.
        """
    )

    scope_content = frontmatter(
        "Game One - Development Scope Notes",
        entry_type="support_note",
        focus="Scope control",
        tags=["AllottaNaut", "Game-One", "Scope", "Development"],
    ) + dedent(
        """\
        # Game One - Development Scope Notes

        ## Scope Control

        Not every chapter needs to become a huge level. Some chapters can be short cinematic
        transitions, dialogue corridors, or small mechanics tests.

        A realistic indie structure could be:

        - Prologue: short cinematic or small ship scene
        - Chapters 1-3: intro void movement and first anchor
        - Chapters 4-5: first formation and walking transition
        - Chapters 6-8: main emotional/puzzle middle
        - Chapters 9-10: nodes and gravity pockets as the largest gameplay section
        - Chapters 11-13: communication, consequence, boundary climax
        - Chapters 14-15: return path and epilogue

        ## What to Avoid

        - Do not over-explain AllottaNaut with technical exposition too early.
        - Do not make AllottaNaut speak fluently too soon.
        - Do not turn the climax into a normal combat boss unless the fight is symbolic and emotionally justified.
        - Do not make Elias purely cold or Rowen purely emotional.
        - Do not let reality-bending solve every problem without cost or rule.
        - Do not make the world feel empty because content is missing; make emptiness feel intentional, unborn, and listening.
        """
    )

    questions_content = frontmatter(
        "Game One - Working Questions",
        entry_type="support_note",
        focus="Open questions",
        tags=["AllottaNaut", "Game-One", "Questions"],
    ) + dedent(
        """\
        # Game One - Working Questions

        These are not blockers, but they should be answered as the story develops.

        - [ ] Are both Elias and Rowen playable from the start, or does the player mainly control one while the other follows?
        - [ ] Is the prologue aboard a ship, a station, or already inside a survey suit outside the vessel?
        - [ ] What is the first object AllottaNaut forms intentionally?
        - [ ] Does AllottaNaut receive its name from the brothers, or was the term already used by their society for the anomaly?
        - [ ] What exact phrase or action teaches AllottaNaut the boundary lesson?
        - [ ] Does their society believe Elias and Rowen when they return?
        - [ ] Does AllottaNaut intentionally send them back, or does it only partially understand what it has done?
        - [ ] What is the first object/shape that remains in AllottaNaut after Elias and Rowen leave?
        """
    )

    return [
        Note(SUPPORT_DIR / "Game One - Mechanics as Story Lessons.md", mechanics_content),
        Note(SUPPORT_DIR / "Game One - Major Themes.md", themes_content),
        Note(SUPPORT_DIR / "Game One - Current Best Ending Shape.md", ending_content),
        Note(SUPPORT_DIR / "Game One - Development Scope Notes.md", scope_content),
        Note(SUPPORT_DIR / "Game One - Working Questions.md", questions_content),
    ]


def all_notes() -> list[Note]:
    return [main_spine_note(), *chapter_notes(), *support_notes()]


def write_note(root: Path, note: Note, overwrite: bool, dry_run: bool) -> str:
    target = root / note.relative_path

    if dry_run:
        if target.exists() and not overwrite:
            return f"SKIP existing: {target}"
        return f"WOULD WRITE: {target}"

    target.parent.mkdir(parents=True, exist_ok=True)

    if target.exists() and not overwrite:
        return f"SKIP existing: {target}"

    target.write_text(note.content, encoding="utf-8")
    return f"WROTE: {target}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create AllottaNaut Game One Obsidian plot notes."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Root folder of your Obsidian vault. Defaults to current working directory.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing notes. Default is safe skip.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview files that would be created without writing them.",
    )

    args = parser.parse_args()
    root = args.root.expanduser().resolve()

    print("AllottaNaut Game One plot note generator")
    print(f"Root: {root}")
    print(f"Overwrite: {args.overwrite}")
    print(f"Dry run: {args.dry_run}")
    print("-" * 72)

    written = 0
    skipped = 0

    for note in all_notes():
        result = write_note(root, note, overwrite=args.overwrite, dry_run=args.dry_run)
        print(result)
        if result.startswith("WROTE") or result.startswith("WOULD WRITE"):
            written += 1
        elif result.startswith("SKIP"):
            skipped += 1

    print("-" * 72)
    if args.dry_run:
        print(f"Dry run complete. Would write {written} file(s); would skip {skipped} existing file(s).")
    else:
        print(f"Done. Wrote {written} file(s); skipped {skipped} existing file(s).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
