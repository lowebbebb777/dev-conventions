"""Attribution guard negative and positive tests."""
from __future__ import annotations
import unittest
from tools.check_commit_attribution import identity_issue, message_issues, range_issues


class AttributionGuardTest(unittest.TestCase):
    def test_human_identity_not_blocked(self):
        self.assertIsNone(identity_issue("Project Owner", "123+owner@users.noreply.github.com"))
        self.assertIsNone(identity_issue("Claude Dupont", "claude@example.com"))

    def test_agent_identity_blocked(self):
        self.assertIsNotNone(identity_issue("Claude", "123+claude@users.noreply.github.com"))
        self.assertIsNotNone(identity_issue("Claude Opus 5.5", "noreply@anthropic.com"))
        self.assertIsNotNone(identity_issue("Codex", "test@example.com"))

    def test_empty_identity_blocked(self):
        self.assertIsNotNone(identity_issue("", "test@example.com"))

    def test_ai_coauthor_blocked(self):
        self.assertTrue(message_issues("Fix\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"))

    def test_human_coauthor_allowed(self):
        self.assertEqual([], message_issues("Fix\nCo-authored-by: Human Tester <tester@example.com>"))

    def test_session_link_blocked(self):
        self.assertTrue(message_issues("Claude-Session: https://claude.ai/code/x"))

    def test_requires_new_commit_range(self):
        with self.assertRaises(ValueError):
            range_issues("HEAD")


if __name__ == "__main__":
    unittest.main()
