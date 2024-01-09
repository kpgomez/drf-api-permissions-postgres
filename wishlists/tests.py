from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Wishlist


# Create your tests here.
class WishlistTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )

        test_user1.save()

        test_toy = Wishlist.objects.create(
            title="doll",
            owner=test_user1,
            description="cute doll"
        )

        test_toy.save()

    def test_wishlist_model(self):
        wishlist = Wishlist.objects.get(id=1)
        actual_owner = str(wishlist.owner)
        actual_title = str(wishlist.title)
        actual_description = str(wishlist.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_title, "doll")
        self.assertEqual(actual_description, "cute doll")

    def test_get_wishlist_list(self):
        url = reverse("wishlist_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        wishlists = response.data
        self.assertEqual(len(wishlists), 1)
        self.assertEqual(wishlists[0]["title"], "doll")

    def test_get_wishlist_by_id(self):
        url = reverse("wishlist_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        wishlists = response.data
        self.assertEqual(wishlists["title", "doll"])

    def test_create_wishlist(self):
        url = reverse("wishlist_list")
        data = {"owner": 1, "title": "baby spoon", "description": "good for baby dolls"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        wishlists = Wishlist.objects.all()
        self.assertEqual(len(wishlists), 2)
        self.assertEqual(Wishlist.objects.get(id=2).title, "baby spoon")

    def test_update_wishlist(self):
        url = reverse("wishlist_detail", args=(1,))
        data = {
            "owner": 1,
            "title": "doll",
            "description": "tangible imaginary friend"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        wishlist = Wishlist.objects.get(id=1)
        self.assertEqual(wishlist.title, data["title"])
        self.assertEqual(wishlist.owner.id, data["owner"])
        self.assertEqual(wishlist.description, data["description"])

    def test_delete_toy(self):
        url = reverse("wishlist_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        wishlists = Wishlist.objects.all()
        self.assertEqual(len(wishlists), 0)
