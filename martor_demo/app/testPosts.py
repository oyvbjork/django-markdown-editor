"""Tests."""
from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    """Test posting.
    """

    def testPost(self):
        """Test posting."""
        post = Post(title="My Title", description="Blurb", wiki="Post Body")
        self.assertEqual(post.title, "My Title")
        self.assertEqual(post.description, "Blurb")
        self.assertEqual(post.wiki, "Post Body")
