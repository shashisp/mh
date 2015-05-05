from tastypie.resources import ModelResource
from campaigns.models import Campaign, Milestone


class CampaignResource(ModelResource):
    class Meta:
        queryset = Campaign.objects.all()
        resource_name = 'campaign'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        always_return_data = True


class MilestoneResource(ModelResource):
	class Meta:
		queryset = Milestone.objects.all()
		resource_name = 'milestone'
		allowed_methods = ['post', 'get', 'patch', 'delete']
        always_return_data = True
