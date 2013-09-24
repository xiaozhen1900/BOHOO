from django.conf.urls import patterns, url

urlpatterns = patterns(
    'groups.views',
    url(r'^new/$', 'new_group', name='new_group'),
    url(r'^edit/(?P<group_id>\d+)/$', 'edit_group', name='edit_group'),
    url(r'^add_avatar/(?P<group_id>\d+)/$', 'add_group_avatar', name='add_group_avatar'),
    url(r'^detail/(?P<group_id>\d+)/$', 'group_detail', name='group_detail'),
    url(r'^ajax_join_group/$', 'ajax_join_group', name='ajax_join_group'),
    url(r'^ajax_apply_join_group/$', 'ajax_apply_join_group', name='ajax_apply_join_group'),
    url(r'^ajax_apply_be_manager/$', 'ajax_apply_be_manager', name='ajax_apply_be_manager'),
    url(r'^ajax_quite_group/$', 'ajax_quite_group', name='ajax_quite_group'),
    url(r'^my_manager/$', 'manage', name='group_my_manage'),
    url(r'^joined/$', 'joined', name='group_joined'),
    url(r'^apply_deal/(?P<group_id>\d+)/$', 'apply_deal', name='apply_deal'),
    url(r'^ajax_apply_pass/$', 'ajax_apply_pass', name='ajax_apply_pass'),
    url(r'^ajax_apply_reject/$', 'ajax_apply_reject', name='ajax_apply_reject'),
    url(r'^add_topic/(?P<group_id>\d+)/$', 'add_topic', name='add_topic'),
    url(r'^delete_topic_image/$', 'ajax_delete_topic_image', name='ajax_delete_topic_image'),
    url(r'^topic/group/$', 'group_topic', name='group_topic'),
    url(r'^topic/created/$', 'created_topic', name='created_topic'),
    url(r'^topic/relied/$', 'replied_topic', name='replied_topic'),
    url(r'^topic/detail/(?P<topic_id>\d+)/$', 'topic_detail', name='topic_detail'),
)
