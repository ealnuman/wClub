app_name='wclub'
app_title='wClub'
app_publisher='Taqrieb Information Technology Company'
app_description='Fighting club & dojo management for Frappe'
app_email='support@taqrieb.com'
app_license='Taqrieb Proprietary License'
fixtures=['Workspace','Workflow','Report','Email Template','Dashboard Chart','Notification',{'doctype':'Role','filters':[ ['role_name','in',['Organization Admin','Club Admin','Coach','Front Desk','Accountant','Member','Parent']] ]}]
app_logo_url='/assets/wclub/images/logo_light.png'
website_context={'favicon':'/assets/wclub/images/favicon.png','brand_html':'<img src="/assets/wclub/images/logo_light.png" height="28">'}
website_route_rules=[{'from_route':'/setup','to_route':'setup/index'},{'from_route':'/portal/my-bookings','to_route':'portal/my-bookings'},{'from_route':'/portal/book','to_route':'portal/book'}]
