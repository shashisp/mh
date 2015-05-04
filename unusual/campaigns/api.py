from tastypie.resources import ModelResource
from campaigns.models import Campaign, Milestone


class CampaignResource(ModelResource):
    class Meta:
        queryset = Campaign.objects.all()
        resource_name = 'campaign'


class MilestoneResource(ModelResource):
	class Meta:
		queryset = Milestone.objects.all()
		resource_name = 'milestone'