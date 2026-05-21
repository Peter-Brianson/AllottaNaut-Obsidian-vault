#!/usr/bin/env python3
"""
setup_allotta_naut_obsidian_vault.py

Drop this file into the root of your local AllottaNaut Obsidian vault Git repo,
then run:

    python setup_allotta_naut_obsidian_vault.py

Default behavior:
- Creates the recommended AllottaNaut franchise-canon vault folder structure.
- Creates starter Markdown files with Obsidian-friendly YAML properties.
- Does NOT overwrite existing files.
- Adds .gitkeep files to folders that may otherwise be empty.

Optional flags:
    --root PATH       Build the vault structure at PATH instead of the current folder.
    --overwrite       Overwrite existing generated Markdown files. Use with caution.
    --dry-run         Show what would be created/skipped without writing files.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent
from typing import Dict, Iterable, List, Tuple


CANON_TAGS = "allotta-naut, canon"


def md(title: str, body: str) -> str:
    """Normalize Markdown text."""
    return dedent(body).strip() + "\n"


FOLDERS: List[str] = [
    "00 - Start Here",
    "01 - Canon Core",
    "02 - Characters",
    "03 - Locations",
    "04 - Games/Game 01 - First Light",
    "04 - Games/Game 02 - Game World Homage",
    "04 - Games/Strange Universe Arc",
    "04 - Games/Cosmic Horror Arc",
    "05 - Timeline",
    "06 - Manuscript and Dialogue",
    "07 - Design Notes",
    "08 - Inspirations and Research",
    "09 - Production Notes",
    "10 - Assets and Visual References",
    "99 - Templates",
    "_attachments",
]


FILES: Dict[str, str] = {
    "README.md": md(
        "README",
        """
        ---
        type: readme
        project: AllottaNaut
        status: active
        tags:
          - allotta-naut
          - vault
        ---

        # AllottaNaut Story Master Vault

        This repository is the Obsidian master vault for the AllottaNaut franchise: canon, characters, systems, locations, timelines, game-specific notes, manuscripts, and production references.

        Start here: [[00 - Start Here/AllottaNaut Master Index|AllottaNaut Master Index]]

        ## Vault Rules

        - Treat [[01 - Canon Core/AllottaNaut|AllottaNaut]] as the living center of the setting.
        - Mark each entry as `canon-core`, `game-specific`, `future-hook`, `draft`, or `experimental`.
        - Keep mechanics tied to story logic whenever possible.
        - Use links aggressively. If a concept matters, give it its own note.
        - Do not delete old ideas immediately. Move them to `experimental` or `retired` status first.
        """,
    ),
    "00 - Start Here/AllottaNaut Master Index.md": md(
        "AllottaNaut Master Index",
        """
        ---
        type: index
        canon_status: canon-core
        project: AllottaNaut
        status: active
        tags:
          - allotta-naut
          - index
          - canon-core
        ---

        # AllottaNaut Master Index

        AllottaNaut is a living reality that begins as an apparent void, learns through observation, and grows by turning contact into connection. This vault exists to keep the franchise coherent across every game.

        ## Core Canon

        - [[01 - Canon Core/AllottaNaut|AllottaNaut]]
        - [[01 - Canon Core/Nodes|Nodes]]
        - [[01 - Canon Core/The Void|The Void]]
        - [[01 - Canon Core/Ghost Mimics|Ghost Mimics]]
        - [[01 - Canon Core/Particle Language|Particle Language]]
        - [[01 - Canon Core/Stimulus Overload|Stimulus Overload]]
        - [[01 - Canon Core/Reality Rewriting|Reality Rewriting]]
        - [[01 - Canon Core/Expulsion|Expulsion]]

        ## Main Characters

        - [[02 - Characters/Elias|Elias]]
        - [[02 - Characters/Rowen|Rowen]]
        - [[02 - Characters/AllottaNaut as Entity|AllottaNaut as Entity]]
        - [[02 - Characters/Future Elias|Future Elias]]
        - [[02 - Characters/Future Rowen|Future Rowen]]

        ## Game One Locations

        - [[03 - Locations/Black Void|Black Void]]
        - [[03 - Locations/Motion Wake|Motion Wake]]
        - [[03 - Locations/Mimicry Field|Mimicry Field]]
        - [[03 - Locations/Childlike Geometry Zone|Childlike Geometry Zone]]
        - [[03 - Locations/Main Node Center|Main Node Center]]
        - [[03 - Locations/Outside Reality|Outside Reality]]

        ## Games and Arcs

        - [[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]
        - [[04 - Games/Game 02 - Game World Homage/Game Two Overview|Game Two - Game World Homage]]
        - [[04 - Games/Strange Universe Arc/Strange Universe Overview|Strange Universe Arc]]
        - [[04 - Games/Cosmic Horror Arc/Cosmic Horror Overview|Cosmic Horror Arc]]

        ## Timeline

        - [[05 - Timeline/Before Game One|Before Game One]]
        - [[05 - Timeline/Game One Timeline|Game One Timeline]]
        - [[05 - Timeline/Between Games|Between Games]]
        - [[05 - Timeline/Long-Term Series Timeline|Long-Term Series Timeline]]

        ## Manuscript and Dialogue

        - [[06 - Manuscript and Dialogue/Game One Intro|Game One Intro]]
        - [[06 - Manuscript and Dialogue/First Mimic Scene|First Mimic Scene]]
        - [[06 - Manuscript and Dialogue/Expulsion Outro|Expulsion Outro]]

        ## Design Notes

        - [[07 - Design Notes/Game One Design Pillars|Game One Design Pillars]]
        - [[07 - Design Notes/Visual Style|Visual Style]]
        - [[07 - Design Notes/Sound and Music|Sound and Music]]
        - [[07 - Design Notes/Mechanics as Lore|Mechanics as Lore]]
        """,
    ),
    "00 - Start Here/How To Use This Vault.md": md(
        "How To Use This Vault",
        """
        ---
        type: guide
        canon_status: meta
        project: AllottaNaut
        status: active
        tags:
          - allotta-naut
          - workflow
        ---

        # How To Use This Vault

        This vault is meant to work as a franchise story bible, design binder, and manuscript database for all future AllottaNaut games.

        ## Daily Workflow

        1. Put new ideas into the correct folder, even if they are rough.
        2. Add `canon_status` to every note.
        3. Link related notes using Obsidian wikilinks like `[[Nodes]]` or `[[Elias]]`.
        4. When an idea becomes official, change its status to `canon-core` or `game-specific`.
        5. If a note becomes obsolete, mark it `retired` instead of deleting it.

        ## Canon Status Values

        - `canon-core`: applies across the franchise.
        - `game-specific`: true inside one game or arc.
        - `future-hook`: likely future canon but not locked.
        - `draft`: active idea, not locked.
        - `experimental`: fun idea, not approved.
        - `retired`: old idea kept for reference.

        ## Suggested Rule

        When in doubt, make a new note. AllottaNaut is a story about connection, so the vault should be built from connected entries.
        """,
    ),
    "00 - Start Here/Canon Status Key.md": md(
        "Canon Status Key",
        """
        ---
        type: reference
        canon_status: meta
        project: AllottaNaut
        status: active
        tags:
          - allotta-naut
          - canon
          - workflow
        ---

        # Canon Status Key

        ## canon-core

        Stable rules, people, places, and truths that should remain true across the whole franchise.

        ## game-specific

        Material that is true for a particular game, but may not define the entire franchise.

        ## future-hook

        Material intended for later games, sequels, supporting roles, or long-term arcs.

        ## draft

        Active development material that can still change.

        ## experimental

        Cool ideas that may or may not become canon.

        ## retired

        Old concepts preserved for reference but no longer part of the active direction.
        """,
    ),
    "01 - Canon Core/AllottaNaut.md": md(
        "AllottaNaut",
        """
        ---
        type: canon-system
        canon_status: canon-core
        project: AllottaNaut
        first_appears: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - canon-core
          - living-reality
        ---

        # AllottaNaut

        ## Short Summary

        AllottaNaut is a living reality that first appears as an empty black void and gradually reveals itself as a naive, responsive, childlike universe learning how to exist through contact.

        ## Core Identity

        AllottaNaut is not simply a place, monster, god, computer, or dream. It is a reality with its own anatomy, memory, senses, and growth process. Everything that enters it becomes part of its experience.

        ## Franchise Role

        AllottaNaut is both setting and character. It can be wondrous, lonely, frightening, playful, dangerous, and innocent at the same time.

        ## Core Rules

        - AllottaNaut learns by observing motion, contact, emotion, language, and pattern.
        - Beings who enter it can become [[Nodes]].
        - It can imitate before it can understand.
        - It can respond before it can explain itself.
        - Its power must have limits so the story does not become deus ex machina.
        - Its growth should feel emotional and experiential, not just mechanical.

        ## Related Entries

        - [[Nodes]]
        - [[The Void]]
        - [[Ghost Mimics]]
        - [[Particle Language]]
        - [[Reality Rewriting]]
        - [[Stimulus Overload]]
        """,
    ),
    "01 - Canon Core/Nodes.md": md(
        "Nodes",
        """
        ---
        type: canon-system
        canon_status: canon-core
        project: AllottaNaut
        tags:
          - allotta-naut
          - nodes
          - canon-core
        ---

        # Nodes

        ## Short Summary

        Nodes are connection points created when beings, places, or realities become part of AllottaNaut's awareness.

        ## Function

        A node is like a neuron, tether, sensory organ, and doorway all at once. Nodes let AllottaNaut perceive beyond itself, remember contact, and eventually communicate with things outside its immediate body.

        ## Game One Usage

        [[Elias]] and [[Rowen]] become the first known human-scale nodes when they enter the void and survive long enough for AllottaNaut to learn from them.

        ## Story Rules

        - A node does not need to be fully controlled by AllottaNaut.
        - Becoming a node should leave a lasting connection.
        - Nodes may allow communication from outside AllottaNaut after expulsion.
        - Nodes should not remove all danger; they create new risks and responsibilities.

        ## Related Entries

        - [[AllottaNaut]]
        - [[Expulsion]]
        - [[Reality Rewriting]]
        """,
    ),
    "01 - Canon Core/The Void.md": md(
        "The Void",
        """
        ---
        type: location-system
        canon_status: canon-core
        project: AllottaNaut
        tags:
          - allotta-naut
          - void
          - canon-core
        ---

        # The Void

        ## Short Summary

        The Void is the first face of AllottaNaut: black emptiness with a single distant center, before shape, language, or understanding fully emerge.

        ## Emotional Purpose

        The Void should begin as frightening and silent, then slowly become lonely, curious, and wondrous.

        ## Game One Purpose

        The opening emptiness gives the player a clean baseline. Every particle, sound, echo, mimic, and geometric response feels meaningful because the world begins with almost nothing.

        ## Related Entries

        - [[AllottaNaut]]
        - [[Black Void]]
        - [[Motion Wake]]
        - [[Main Node Center]]
        """,
    ),
    "01 - Canon Core/Ghost Mimics.md": md(
        "Ghost Mimics",
        """
        ---
        type: canon-mechanic
        canon_status: canon-core
        project: AllottaNaut
        tags:
          - allotta-naut
          - ghost-mimics
          - mechanics-as-lore
        ---

        # Ghost Mimics

        ## Short Summary

        Ghost Mimics are AllottaNaut's early attempts to copy the brothers' movement, shape, and behavior before it understands identity or intention.

        ## Story Purpose

        Ghost Mimics turn simple movement into first contact. At first they may feel eerie, but over time the player should understand that the mimics are not hunting them. They are learning.

        ## Gameplay Purpose

        - Show the player's movement history as echo geometry.
        - Let particles imitate walking, turning, jumping, stopping, and approaching.
        - Create moments where [[Elias]] and [[Rowen]] realize they are being copied.
        - Build toward communication through motion.

        ## Risk

        The mimic system can become threatening if AllottaNaut copies without understanding consequences.

        ## Related Entries

        - [[Particle Language]]
        - [[Motion Wake]]
        - [[Mimicry Field]]
        - [[Mechanics as Lore]]
        """,
    ),
    "01 - Canon Core/Particle Language.md": md(
        "Particle Language",
        """
        ---
        type: canon-system
        canon_status: canon-core
        project: AllottaNaut
        tags:
          - allotta-naut
          - particle-language
          - communication
        ---

        # Particle Language

        ## Short Summary

        Particle Language is the first nonverbal communication between the brothers and AllottaNaut.

        ## Function

        Before words, AllottaNaut responds through particles, echoes, geometry, rhythm, direction, density, brightness, and motion trails.

        ## Game One Usage

        The player teaches AllottaNaut by moving. Motion causes response. Repeated actions create patterns. Patterns become meaning.

        ## Design Notes

        - Communication should feel discovered, not tutorialized too heavily.
        - Particle responses should become more intentional as the game progresses.
        - The language should preserve a feeling of childlike wonder.

        ## Related Entries

        - [[Ghost Mimics]]
        - [[Motion Wake]]
        - [[Childlike Geometry Zone]]
        """,
    ),
    "01 - Canon Core/Stimulus Overload.md": md(
        "Stimulus Overload",
        """
        ---
        type: canon-system
        canon_status: canon-core
        project: AllottaNaut
        tags:
          - allotta-naut
          - stimulus-overload
          - expulsion
        ---

        # Stimulus Overload

        ## Short Summary

        Stimulus Overload occurs when AllottaNaut receives too much sensation, meaning, motion, and identity too quickly.

        ## Game One Purpose

        Stimulus Overload creates the reason the brothers are expelled near the end of Game One. AllottaNaut wants connection, but it cannot yet safely hold everything it is learning.

        ## Story Tone

        This should feel less like punishment and more like an involuntary sneeze, panic response, or overwhelmed child pushing everything away.

        ## Related Entries

        - [[Expulsion]]
        - [[Main Node Center]]
        - [[AllottaNaut]]
        """,
    ),
    "01 - Canon Core/Reality Rewriting.md": md(
        "Reality Rewriting",
        """
        ---
        type: canon-system
        canon_status: canon-core
        project: AllottaNaut
        tags:
          - allotta-naut
          - reality-rewriting
          - soft-magic
        ---

        # Reality Rewriting

        ## Short Summary

        Reality Rewriting is AllottaNaut's ability to alter its own body, rules, appearance, and connections as it learns.

        ## Rule Balance

        Reality Rewriting should be powerful, but not unlimited. AllottaNaut can reshape itself more easily than it can reshape outside realities. Its understanding, emotional state, and node connections limit what it can do.

        ## Franchise Use

        This is the bridge between walking-simulator wonder, game-world homage, strange universes, and later cosmic-scale stories.

        ## Limiters

        - It must perceive or connect before it can alter.
        - It can imitate wrong.
        - It can misunderstand intent.
        - Too much input can cause [[Stimulus Overload]].
        - Nodes create access but not perfect control.

        ## Related Entries

        - [[AllottaNaut]]
        - [[Nodes]]
        - [[Mechanics as Lore]]
        """,
    ),
    "01 - Canon Core/Expulsion.md": md(
        "Expulsion",
        """
        ---
        type: canon-event
        canon_status: canon-core
        project: AllottaNaut
        first_appears: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - expulsion
          - game-one
        ---

        # Expulsion

        ## Short Summary

        Expulsion is the moment AllottaNaut ejects the brothers back out of itself after becoming overwhelmed by stimulus.

        ## Story Function

        This ends Game One while preserving the relationship. The brothers are separated from AllottaNaut physically, but they are not fully disconnected.

        ## Tone

        It should feel sudden, strange, and almost comedic in physical logic, but emotionally bittersweet.

        ## Future Hook

        After expulsion, the brothers can still communicate with AllottaNaut because they have become [[Nodes]].

        ## Related Entries

        - [[Stimulus Overload]]
        - [[Nodes]]
        - [[Expulsion Outro]]
        """,
    ),
    "02 - Characters/Elias.md": md(
        "Elias",
        """
        ---
        type: character
        canon_status: canon-core
        project: AllottaNaut
        first_appears: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        role: protagonist
        tags:
          - allotta-naut
          - character
          - game-one
        ---

        # Elias

        ## Short Summary

        Elias is one of the two brothers pulled into AllottaNaut during first contact.

        ## Core Role

        Elias should lean toward reason, observation, caution, and interpretation. He helps frame the void as something that might be studied, not merely survived.

        ## Game One Arc

        Elias begins by treating AllottaNaut like an anomaly. Over time, he realizes it is not just a problem or place, but a living reality trying to learn.

        ## Relationships

        - [[Rowen]]: brother, emotional counterweight, trusted companion.
        - [[AllottaNaut as Entity]]: first-contact subject that becomes something closer to a strange child or living world.

        ## Future Series Role

        Elias can become a support or teacher figure for later protagonists, similar to a guide who understands AllottaNaut's risks and rules.
        """,
    ),
    "02 - Characters/Rowen.md": md(
        "Rowen",
        """
        ---
        type: character
        canon_status: canon-core
        project: AllottaNaut
        first_appears: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        role: protagonist
        tags:
          - allotta-naut
          - character
          - game-one
        ---

        # Rowen

        ## Short Summary

        Rowen is one of the two brothers pulled into AllottaNaut during first contact.

        ## Core Role

        Rowen should lean toward instinct, humor, emotion, and direct interaction. Where Elias observes, Rowen tests, reacts, and plays.

        ## Game One Arc

        Rowen begins by responding emotionally to the emptiness and danger. Over time, his movement and playfulness become part of how the brothers communicate with AllottaNaut.

        ## Relationships

        - [[Elias]]: brother, stabilizing presence, intellectual counterweight.
        - [[AllottaNaut as Entity]]: strange living reality that learns through copying his behavior.

        ## Future Series Role

        Rowen can become a more approachable support figure for later protagonists, translating AllottaNaut's weirdness into practical survival and emotional sense.
        """,
    ),
    "02 - Characters/AllottaNaut as Entity.md": md(
        "AllottaNaut as Entity",
        """
        ---
        type: character
        canon_status: canon-core
        project: AllottaNaut
        aliases:
          - AllottaNaut
          - The Living Reality
        role: living-setting
        tags:
          - allotta-naut
          - character
          - living-reality
        ---

        # AllottaNaut as Entity

        ## Short Summary

        AllottaNaut is the living reality at the center of the franchise, acting as both world and character.

        ## Personality Direction

        - Naive but not stupid.
        - Lonely but not purely sad.
        - Playful but dangerous by accident.
        - Curious before moral.
        - Childlike without becoming childish.

        ## Emotional Core

        AllottaNaut wants connection before it understands what connection costs.

        ## Character Growth

        - Empty awareness.
        - Motion response.
        - Mimicry.
        - Pattern recognition.
        - Communication.
        - Emotional attachment.
        - Overload.
        - Long-distance contact through nodes.
        - Later responsibility for its own power.

        ## Related Entries

        - [[AllottaNaut]]
        - [[Nodes]]
        - [[Reality Rewriting]]
        """,
    ),
    "02 - Characters/Future Elias.md": md(
        "Future Elias",
        """
        ---
        type: character-state
        canon_status: future-hook
        project: AllottaNaut
        based_on: "[[Elias]]"
        tags:
          - allotta-naut
          - future-hook
          - support-role
        ---

        # Future Elias

        ## Short Summary

        Future Elias is the later-series version of Elias after Game One, serving more as a teacher, support voice, researcher, or navigator than a main protagonist.

        ## Possible Function

        - Explains AllottaNaut's rules without removing mystery.
        - Warns new protagonists about overstimulation, mimicry, and node consequences.
        - Helps maintain franchise continuity.
        - Carries emotional weight from first contact.
        """,
    ),
    "02 - Characters/Future Rowen.md": md(
        "Future Rowen",
        """
        ---
        type: character-state
        canon_status: future-hook
        project: AllottaNaut
        based_on: "[[Rowen]]"
        tags:
          - allotta-naut
          - future-hook
          - support-role
        ---

        # Future Rowen

        ## Short Summary

        Future Rowen is the later-series version of Rowen after Game One, serving as a more relaxed, practical, emotionally grounded support figure.

        ## Possible Function

        - Helps new characters deal with fear and confusion.
        - Understands AllottaNaut through behavior and feeling more than theory.
        - Provides warmth, humor, and human grounding.
        - Reminds the series that wonder matters as much as danger.
        """,
    ),
    "03 - Locations/Black Void.md": md(
        "Black Void",
        """
        ---
        type: location
        canon_status: game-specific
        project: AllottaNaut
        game: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - location
          - game-one
        ---

        # Black Void

        ## Short Summary

        The Black Void is the opening environment of Game One: empty, silent, and almost featureless except for the distant presence of the main node.

        ## Player Experience

        The player should feel alone at first, then gradually notice that movement has consequences.

        ## Related Entries

        - [[The Void]]
        - [[Motion Wake]]
        - [[Game One Intro]]
        """,
    ),
    "03 - Locations/Motion Wake.md": md(
        "Motion Wake",
        """
        ---
        type: location
        canon_status: game-specific
        project: AllottaNaut
        game: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - location
          - particle-language
        ---

        # Motion Wake

        ## Short Summary

        The Motion Wake is the first area where the brothers' movement creates visible response: particles, trails, pulses, and echoes.

        ## Purpose

        This area turns movement into communication. The player learns that the void is not dead.

        ## Related Entries

        - [[Particle Language]]
        - [[Ghost Mimics]]
        - [[Mechanics as Lore]]
        """,
    ),
    "03 - Locations/Mimicry Field.md": md(
        "Mimicry Field",
        """
        ---
        type: location
        canon_status: game-specific
        project: AllottaNaut
        game: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - location
          - ghost-mimics
        ---

        # Mimicry Field

        ## Short Summary

        The Mimicry Field is where AllottaNaut's copying becomes clear enough that the brothers realize they are being studied.

        ## Purpose

        This is the turning point from strange environmental response to recognizable first contact.

        ## Related Entries

        - [[Ghost Mimics]]
        - [[First Mimic Scene]]
        """,
    ),
    "03 - Locations/Childlike Geometry Zone.md": md(
        "Childlike Geometry Zone",
        """
        ---
        type: location
        canon_status: game-specific
        project: AllottaNaut
        game: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - location
          - geometry
          - wonder
        ---

        # Childlike Geometry Zone

        ## Short Summary

        The Childlike Geometry Zone is where AllottaNaut begins forming simple shapes, structures, and playful geometric imitations.

        ## Visual Tone

        Minimal, primitive, whimsical, colorful in moderation, and emotionally warm without losing the strangeness of the void.

        ## Related Entries

        - [[Visual Style]]
        - [[Particle Language]]
        - [[Main Node Center]]
        """,
    ),
    "03 - Locations/Main Node Center.md": md(
        "Main Node Center",
        """
        ---
        type: location
        canon_status: game-specific
        project: AllottaNaut
        game: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - location
          - main-node
        ---

        # Main Node Center

        ## Short Summary

        The Main Node Center is the largest visible particle mass near the heart of AllottaNaut in Game One.

        ## Story Function

        Reaching the center marks the brothers' deepest contact with AllottaNaut before stimulus overload forces expulsion.

        ## Related Entries

        - [[Stimulus Overload]]
        - [[Expulsion]]
        - [[Expulsion Outro]]
        """,
    ),
    "03 - Locations/Outside Reality.md": md(
        "Outside Reality",
        """
        ---
        type: location
        canon_status: canon-core
        project: AllottaNaut
        tags:
          - allotta-naut
          - location
          - outside-reality
        ---

        # Outside Reality

        ## Short Summary

        Outside Reality is the normal universe the brothers come from, including their advanced civilization and the Dyson-scale society they belong to.

        ## Franchise Purpose

        This is the grounded contrast to AllottaNaut's living void. It also allows communication and consequences after Game One.

        ## Related Entries

        - [[Before Game One]]
        - [[Between Games]]
        - [[Nodes]]
        """,
    ),
    "04 - Games/Game 01 - First Light/Game One Overview.md": md(
        "Game One Overview",
        """
        ---
        type: game-overview
        canon_status: game-specific
        project: AllottaNaut
        working_title: First Light
        status: draft
        tags:
          - allotta-naut
          - game-one
          - overview
        ---

        # Game One - First Light

        ## Short Summary

        Game One follows [[Elias]] and [[Rowen]] as they are pulled into an empty black void and slowly discover that the void is [[AllottaNaut]], a living reality learning from them.

        ## Target Experience

        A short, third-person, semi-walking-simulator first-contact story built on wonder, loneliness, primitive geometry, particle effects, and emotional discovery.

        ## Core Progression

        1. Blank void.
        2. Movement creates particle response.
        3. Particles imitate the brothers.
        4. Mimicry becomes communication.
        5. The world becomes more playful and geometric.
        6. The brothers approach the [[Main Node Center]].
        7. [[Stimulus Overload]] causes [[Expulsion]].
        8. The brothers realize the connection remains through [[Nodes]].

        ## Design Pillars

        - Wonder over spectacle.
        - Emotion over exposition.
        - Mechanics as lore.
        - Simple visuals with strong mood.
        - First contact as a relationship, not a puzzle box.
        """,
    ),
    "04 - Games/Game 02 - Game World Homage/Game Two Overview.md": md(
        "Game Two Overview",
        """
        ---
        type: game-overview
        canon_status: future-hook
        project: AllottaNaut
        status: experimental
        tags:
          - allotta-naut
          - future-hook
          - game-two
        ---

        # Game Two - Game World Homage

        ## Short Summary

        A possible sequel where characters enter a world shaped by classic video game logic and become aware they are moving through a constructed game-like reality.

        ## Purpose

        This concept lets AllottaNaut explore rules, quests, levels, NPC behavior, genre logic, and player expectation as things it is learning to imitate.

        ## Support Role Hook

        [[Future Elias]] and [[Future Rowen]] can take a backseat teacher/support role instead of being the main playable characters.
        """,
    ),
    "04 - Games/Strange Universe Arc/Strange Universe Overview.md": md(
        "Strange Universe Overview",
        """
        ---
        type: game-arc
        canon_status: future-hook
        project: AllottaNaut
        status: experimental
        tags:
          - allotta-naut
          - future-hook
          - strange-universes
        ---

        # Strange Universe Arc

        ## Short Summary

        A future arc where characters become protected nodes of AllottaNaut while traveling through strange universes and hostile planets.

        ## Rule Hook

        AllottaNaut can protect characters from some reality-altering effects, such as not needing to breathe, but cannot prevent direct physical harm like crushing, slicing, burning, or impact.

        ## Inspiration Direction

        Rain World, Scavengers Reign, Samurai Jack, The Midnight Gospel, Fantastic Planet, and abstract geometry worlds.
        """,
    ),
    "04 - Games/Cosmic Horror Arc/Cosmic Horror Overview.md": md(
        "Cosmic Horror Overview",
        """
        ---
        type: game-arc
        canon_status: future-hook
        project: AllottaNaut
        status: experimental
        tags:
          - allotta-naut
          - future-hook
          - cosmic-horror
        ---

        # Cosmic Horror Arc

        ## Short Summary

        A future arc where AllottaNaut encounters or absorbs a universe-eating entity, turning cosmic horror into a test of growth, limits, and responsibility.

        ## Franchise Purpose

        This arc should show that AllottaNaut can grow powerful without becoming an easy answer to every problem.

        ## Rule Concern

        Keep power scaling emotional and constrained. AllottaNaut should not become a universal reset button.
        """,
    ),
    "05 - Timeline/Before Game One.md": md(
        "Before Game One",
        """
        ---
        type: timeline
        canon_status: canon-core
        project: AllottaNaut
        tags:
          - allotta-naut
          - timeline
          - before-game-one
        ---

        # Before Game One

        ## Known Beats

        - The brothers come from an advanced democratic, council-driven civilization.
        - Their society is approaching or operating at Type II scale.
        - A Dyson sphere or Dyson-swarm-like project is underway, with some power already online.
        - Near-light travel exists.
        - Time travel does not exist.
        - Teleportation may be ethically debated, but should not dominate Game One.
        - [[Elias]] and [[Rowen]] encounter the anomaly that pulls them into [[The Void]].
        """,
    ),
    "05 - Timeline/Game One Timeline.md": md(
        "Game One Timeline",
        """
        ---
        type: timeline
        canon_status: game-specific
        project: AllottaNaut
        game: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - timeline
          - game-one
        ---

        # Game One Timeline

        ## Core Sequence

        1. Elias and Rowen are pulled into the blank void.
        2. They orient themselves in silence and emptiness.
        3. Movement creates the first particles.
        4. Particle responses form the [[Motion Wake]].
        5. [[Ghost Mimics]] begin copying the brothers.
        6. The brothers recognize that the void is responding.
        7. The world develops more playful geometry.
        8. The brothers approach the [[Main Node Center]].
        9. AllottaNaut reaches [[Stimulus Overload]].
        10. [[Expulsion]] ejects the brothers.
        11. The ending reveals the connection remains through [[Nodes]].
        """,
    ),
    "05 - Timeline/Between Games.md": md(
        "Between Games",
        """
        ---
        type: timeline
        canon_status: future-hook
        project: AllottaNaut
        tags:
          - allotta-naut
          - timeline
          - between-games
        ---

        # Between Games

        ## Possible Beats

        - Elias and Rowen recover from expulsion.
        - They realize AllottaNaut can still communicate in limited ways.
        - Their civilization debates what happened.
        - AllottaNaut begins reaching beyond its original void through node connections.
        - Elias and Rowen shift from protagonists to support figures.
        """,
    ),
    "05 - Timeline/Long-Term Series Timeline.md": md(
        "Long-Term Series Timeline",
        """
        ---
        type: timeline
        canon_status: future-hook
        project: AllottaNaut
        tags:
          - allotta-naut
          - timeline
          - franchise
        ---

        # Long-Term Series Timeline

        ## Draft Arc

        1. First contact with AllottaNaut.
        2. Node communication after expulsion.
        3. New protagonists interact with AllottaNaut from different angles.
        4. AllottaNaut experiments with game-like rules and other realities.
        5. AllottaNaut learns responsibility and restraint.
        6. Later cosmic-scale threats test the limits of its growth.
        """,
    ),
    "06 - Manuscript and Dialogue/Game One Intro.md": md(
        "Game One Intro",
        """
        ---
        type: manuscript-scene
        canon_status: draft
        project: AllottaNaut
        game: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - manuscript
          - game-one
        ---

        # Game One Intro

        ## Scene Purpose

        Establish Elias and Rowen, their brother dynamic, their advanced but human perspective, and the shock of being pulled into a void with no familiar reference points.

        ## Emotional Beat

        Start with confusion and fear. End the intro with the first tiny sign that the void responds.

        ## Draft Notes

        - Avoid heavy exposition at the start.
        - Let the brothers' reactions teach the player who they are.
        - Keep the first particle event small and intimate.
        """,
    ),
    "06 - Manuscript and Dialogue/First Mimic Scene.md": md(
        "First Mimic Scene",
        """
        ---
        type: manuscript-scene
        canon_status: draft
        project: AllottaNaut
        game: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - manuscript
          - ghost-mimics
        ---

        # First Mimic Scene

        ## Scene Purpose

        The brothers realize the particles are not random. Something is copying them.

        ## Emotional Beat

        Eerie imitation becomes fragile first contact.

        ## Dialogue Direction

        - Elias should try to explain what is happening.
        - Rowen should test it with movement, humor, or a simple repeated gesture.
        - AllottaNaut should answer through shape, timing, and echo, not words.
        """,
    ),
    "06 - Manuscript and Dialogue/Expulsion Outro.md": md(
        "Expulsion Outro",
        """
        ---
        type: manuscript-scene
        canon_status: draft
        project: AllottaNaut
        game: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - manuscript
          - expulsion
        ---

        # Expulsion Outro

        ## Scene Purpose

        End Game One by ejecting the brothers from AllottaNaut while preserving the emotional connection.

        ## Emotional Beat

        The ending should be bittersweet: sudden separation, awe, relief, and the realization that the relationship is not over.

        ## Future Hook

        The brothers discover they are still connected as [[Nodes]].
        """,
    ),
    "07 - Design Notes/Game One Design Pillars.md": md(
        "Game One Design Pillars",
        """
        ---
        type: design-note
        canon_status: game-specific
        project: AllottaNaut
        game: "[[04 - Games/Game 01 - First Light/Game One Overview|Game One - First Light]]"
        tags:
          - allotta-naut
          - design
          - game-one
        ---

        # Game One Design Pillars

        ## Pillars

        - Wonder first.
        - Minimalism with emotional payoff.
        - Movement as language.
        - Particles as response.
        - Geometry as thought.
        - AllottaNaut is a living character, not just a backdrop.
        - The story should feel family-friendly but not shallow.
        - Avoid overexplaining the mystery.
        """,
    ),
    "07 - Design Notes/Visual Style.md": md(
        "Visual Style",
        """
        ---
        type: design-note
        canon_status: game-specific
        project: AllottaNaut
        tags:
          - allotta-naut
          - visual-style
          - art-direction
        ---

        # Visual Style

        ## Direction

        Low-poly, primitive, flat-color, minimal, whimsical, and readable. The tone should be closer to wonder than realism.

        ## References

        - Cozy exploration feel similar in spirit to A Short Hike.
        - Wonder and warmth inspired by Disney/Ghibli emotional environments.
        - Strange-world inspiration from Rain World, Scavengers Reign, Samurai Jack, The Midnight Gospel, and Fantastic Planet.

        ## Game One Rule

        Start nearly empty. Add complexity only as AllottaNaut learns.
        """,
    ),
    "07 - Design Notes/Sound and Music.md": md(
        "Sound and Music",
        """
        ---
        type: design-note
        canon_status: game-specific
        project: AllottaNaut
        tags:
          - allotta-naut
          - sound
          - music
        ---

        # Sound and Music

        ## Direction

        Sound should evolve alongside AllottaNaut's awareness. Early sound is sparse, distant, and almost absent. Later sound becomes rhythmic, curious, and melodic.

        ## Motif Idea

        A recurring space-shanty-like motif may become the franchise theme, possibly introduced near or after expulsion and developed in later games.

        ## Sound Rules

        - Particle responses should have delicate, readable audio cues.
        - Mimics should feel eerie before they feel playful.
        - The center should feel overwhelming without becoming harsh noise.
        """,
    ),
    "07 - Design Notes/Mechanics as Lore.md": md(
        "Mechanics as Lore",
        """
        ---
        type: design-note
        canon_status: canon-core
        project: AllottaNaut
        tags:
          - allotta-naut
          - mechanics-as-lore
          - design
        ---

        # Mechanics as Lore

        ## Core Principle

        Whenever possible, a gameplay mechanic should also explain something about AllottaNaut.

        ## Examples

        - Particle trails show AllottaNaut perceiving motion.
        - Ghost mimics show imitation before understanding.
        - Geometry growth shows learning.
        - Stimulus overload explains the end-state expulsion.
        - Save continuity can represent lasting node connection across games.

        ## Rule

        A mechanic is stronger when it feels like AllottaNaut doing something, not just the game system doing something.
        """,
    ),
    "08 - Inspirations and Research/Inspiration Index.md": md(
        "Inspiration Index",
        """
        ---
        type: index
        canon_status: meta
        project: AllottaNaut
        tags:
          - allotta-naut
          - inspirations
          - research
        ---

        # Inspiration Index

        ## Tone and Feel

        - A Short Hike: small-scope cozy exploration.
        - Disney/Ghibli: whimsy, warmth, wonder, childlike emotional clarity.

        ## Strange Worlds

        - Rain World
        - Scavengers Reign
        - Samurai Jack
        - The Midnight Gospel
        - Fantastic Planet

        ## Usage Rule

        Inspirations should guide emotional and visual language without becoming direct copies.
        """,
    ),
    "09 - Production Notes/GitHub Workflow.md": md(
        "GitHub Workflow",
        """
        ---
        type: production-note
        canon_status: meta
        project: AllottaNaut
        tags:
          - allotta-naut
          - github
          - workflow
        ---

        # GitHub Workflow

        ## Basic Loop

        1. Edit notes in Obsidian.
        2. Review changed files.
        3. Commit with a clear message.
        4. Push to GitHub.
        5. Ask ChatGPT to inspect the repo when needed.

        ## Suggested Commit Messages

        - `Add initial canon core notes`
        - `Expand Game One timeline`
        - `Draft Elias and Rowen character arcs`
        - `Add future sequel hooks`
        """,
    ),
    "10 - Assets and Visual References/Visual Reference Index.md": md(
        "Visual Reference Index",
        """
        ---
        type: index
        canon_status: meta
        project: AllottaNaut
        tags:
          - allotta-naut
          - visual-reference
          - assets
        ---

        # Visual Reference Index

        Put concept art, screenshots, model references, particle studies, and style notes here.

        ## Suggested Sections

        - Elias references
        - Rowen references
        - Suit/model references
        - Void screenshots
        - Particle effect concepts
        - Main node concepts
        - PS1-era/simple model references
        """,
    ),
    "99 - Templates/Character Template.md": md(
        "Character Template",
        """
        ---
        type: character
        canon_status: draft
        project: AllottaNaut
        first_appears:
        role:
        status: draft
        tags:
          - allotta-naut
          - character
        ---

        # Character Name

        ## Short Summary

        ## Core Identity

        ## Role in the Franchise

        ## Role in Current Game

        ## Personality

        ## Relationships

        ## Arc

        ## Visual Notes

        ## Related Entries
        """,
    ),
    "99 - Templates/Location Template.md": md(
        "Location Template",
        """
        ---
        type: location
        canon_status: draft
        project: AllottaNaut
        first_appears:
        status: draft
        tags:
          - allotta-naut
          - location
        ---

        # Location Name

        ## Short Summary

        ## Emotional Purpose

        ## Visual Design

        ## Story Function

        ## Gameplay Function

        ## Related Entries
        """,
    ),
    "99 - Templates/System Template.md": md(
        "System Template",
        """
        ---
        type: canon-system
        canon_status: draft
        project: AllottaNaut
        status: draft
        tags:
          - allotta-naut
          - system
        ---

        # System Name

        ## Short Summary

        ## What It Does

        ## Story Rules

        ## Gameplay Rules

        ## Limits

        ## Related Entries
        """,
    ),
    "99 - Templates/Game Template.md": md(
        "Game Template",
        """
        ---
        type: game-overview
        canon_status: draft
        project: AllottaNaut
        status: draft
        tags:
          - allotta-naut
          - game
        ---

        # Game Title

        ## Short Summary

        ## Player Fantasy

        ## Core Loop

        ## Story Arc

        ## Characters

        ## Locations

        ## Mechanics

        ## Ending Hook
        """,
    ),
    "99 - Templates/Timeline Event Template.md": md(
        "Timeline Event Template",
        """
        ---
        type: timeline-event
        canon_status: draft
        project: AllottaNaut
        era:
        status: draft
        tags:
          - allotta-naut
          - timeline
        ---

        # Timeline Event

        ## Date or Era

        ## Event Summary

        ## Cause

        ## Consequence

        ## Related Entries
        """,
    ),
}


def write_file(path: Path, content: str, overwrite: bool, dry_run: bool) -> str:
    if path.exists() and not overwrite:
        return "skipped"
    if dry_run:
        return "would overwrite" if path.exists() else "would create"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return "overwritten" if path.exists() and overwrite else "created"


def create_folders(root: Path, folders: Iterable[str], dry_run: bool) -> List[Tuple[str, str]]:
    results: List[Tuple[str, str]] = []
    for folder in folders:
        folder_path = root / folder
        if folder_path.exists():
            results.append((folder, "exists"))
            continue
        if dry_run:
            results.append((folder, "would create"))
        else:
            folder_path.mkdir(parents=True, exist_ok=True)
            results.append((folder, "created"))
    return results


def add_gitkeep_files(root: Path, folders: Iterable[str], dry_run: bool) -> List[Tuple[str, str]]:
    results: List[Tuple[str, str]] = []
    for folder in folders:
        gitkeep_path = root / folder / ".gitkeep"
        if gitkeep_path.exists():
            results.append((str(gitkeep_path.relative_to(root)), "exists"))
            continue
        if dry_run:
            results.append((str(gitkeep_path.relative_to(root)), "would create"))
        else:
            gitkeep_path.parent.mkdir(parents=True, exist_ok=True)
            gitkeep_path.write_text("", encoding="utf-8")
            results.append((str(gitkeep_path.relative_to(root)), "created"))
    return results


def build_vault(root: Path, overwrite: bool, dry_run: bool) -> None:
    root = root.resolve()
    print(f"AllottaNaut Obsidian vault setup")
    print(f"Root: {root}")
    print(f"Overwrite existing files: {overwrite}")
    print(f"Dry run: {dry_run}")
    print()

    folder_results = create_folders(root, FOLDERS, dry_run)
    print("Folders:")
    for folder, status in folder_results:
        print(f"  [{status}] {folder}")

    print("\nMarkdown files:")
    created = skipped = overwritten = would = 0
    for relative_path, content in FILES.items():
        output_path = root / relative_path
        already_exists = output_path.exists()

        if already_exists and not overwrite:
            status = "skipped"
            skipped += 1
        elif dry_run:
            status = "would overwrite" if already_exists else "would create"
            would += 1
        else:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(content, encoding="utf-8", newline="\n")
            if already_exists:
                status = "overwritten"
                overwritten += 1
            else:
                status = "created"
                created += 1

        print(f"  [{status}] {relative_path}")

    gitkeep_results = add_gitkeep_files(root, FOLDERS, dry_run)
    print("\n.gitkeep files:")
    for relative_path, status in gitkeep_results:
        print(f"  [{status}] {relative_path}")

    print("\nSummary:")
    print(f"  Created files: {created}")
    print(f"  Overwritten files: {overwritten}")
    print(f"  Skipped existing files: {skipped}")
    if dry_run:
        print(f"  Would write files: {would}")

    print("\nNext steps:")
    print("  1. Open this folder in Obsidian as a vault.")
    print("  2. Review the generated notes.")
    print("  3. Commit and push to GitHub:")
    print("       git add .")
    print('       git commit -m "Add AllottaNaut Obsidian vault starter structure"')
    print("       git push")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create the starter Obsidian vault structure for the AllottaNaut story master vault."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Vault/repo root. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing generated Markdown files. Default is to skip existing files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    build_vault(args.root, overwrite=args.overwrite, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
