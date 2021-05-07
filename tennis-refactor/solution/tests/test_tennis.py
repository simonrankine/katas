from unittest import TestCase, mock

from tennis import Player, Point


class TestPlayer(TestCase):

    def setUp(self):
        self.uut = Player()

    def test_increment_point_from_zero(self):
        self.uut.increment_points()
        self.assertEqual(self.uut.points, 15)

    def test_increment_point_from_fifteen(self):
        self.uut.points = 15

        self.uut.increment_points()
        self.assertEqual(self.uut.points, 30)


class TestPoint(TestCase):


    def setUp(self):
        self.winner = mock.MagicMock()
        self.loser = mock.MagicMock()
        self.uut = Point(self.winner, self.loser)

    def test_add_points(self):
        self.winner.points = 20
        self.uut.add_points()
        self.winner.increment_points.assert_called_once()
