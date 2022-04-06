from rest_framework import routers

from support.views import CommentViewset, TicketViewset

router = routers.SimpleRouter()
router.register(r'comment', CommentViewset)
router.register(r'ticket', TicketViewset)