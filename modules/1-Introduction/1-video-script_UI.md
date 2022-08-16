## Scenario
- Quick overview to familarise usesr with UI
- Log into demo instance https://demo.netbox.dev/

In this demo video we will log into the public demo instance of NetBox which is freely available to use @ demo.netbox.dev. Once logged in, you are presented with a menu system on the left had side of the screen. Starting at the top, you can see that under this first section NetBox is tracking the objects that make up the organization - and this can include objects like the Regions and Sites that the network devices are physically located at, along with the racks that devices are installed in. This section also includes Tenant information so you can define which customers or departments you have, plus all the contact information for your organization.

Moving down the menu. you have Devices. With devices you always start with a manufacturer - so if I click on Manufacturers, then Cisco for example you can see the Cisco Device types we have set up in the demo instance, and then we can drill down further, for example into the C9200-48P device type, and there are 13 instances of this particular device type.  So if we click on the first instance of this device type we can take a look at the details we have stored for it for example the region, site and the rack. Over on the right hand side in the management panel we can see that device role is an Access Switch, and if we had a primary IPv4 or v6 IP addresses configured they would also be visible here.  

We can also click on the interfaces tab to see details of all the configured interfaces and as we have defined cables and connections we can even bring up a visual of the cable trace for interface GigabitEthernet1/0/1 which we can see connects directly to a router in the same Communications closet. Devices is also where you define all the other possible objects that a device might have - ranging from the platform it is running on for example Cisco IOS through to physical components such as interfaces, console ports and module bays. 

Moving down the menu again, you have the Connections section where you define all the physical connections in your network. For example in Cables - we can click on the first cable in the list and see that the cable is a yellow, single mode fiber cable that connects from the Level 3 circuit into the interface on our router at DM-Stanford site.  Also notice the blue 'upload' symbol next to cables - whenever you see this you can do a bulk import of objects into the database either by adding the CSV data manually or uploading a CSV file with the options section telling you which are the required fields.

Next we have interface connections - which tell you which interfaces on which devices are connected to other devices and on which ports. You can also model Wireless links, console and power connections. 

The Wireless section is used to model all of you wireless networks - if we click on add you can see we can track all data related to your SSID's including what VLAN is used, which site the network is linked to and also the authentication settings used, including the pre-shared key.  

The next big section is IPAM, as you would expect there are a lot of object types that can be stored in here as this is where NetBox creates an authoritative network source of truth for the ideal state of your IP addresses. It tells you how things should be, or how you want them to be. As IP addressing is hierarchical, in NetBox you can model everything starting from the highest level of the Regional Internet Registries, like ARIN, through RFC1918 private address space and further down into aggregates, and then through to prefixes, IP ranges and right down to individual IP addresses. At the level of the IP address you can track a whole range of information relating to the IP itself such as the DNS name, the interface assignment and also any network address translation that you have in place.

This just scratches the surface of the IPAM section of the database but we will return to it in later modules of this course.

Under Virtualization, NetBox can model your virtual machines, starting with defining your cluster types such as VMware or other well known cloud platforms, and then adding your actual VM's - where you can define all the data that you can with a network device such as interfaces and device role, but you can also define things like resources such as CPU and memory

Circuits is where you store all the information relating to your providers and circuits - how many times as network engineers do we struggle to find the contact information to raise a support ticket with a provider when a circuit goes down at a DC or a remote site? well those days are over as NetBox stores all the relevant information and makes it incredibly easy to find!

Another great feature of NetBox is the ability to track your power feeds and power panels - again as with all the data stored in NetBox it is super easy to track and find exactly the data you need with the intuitive UI. 

So the last section of the left hand menu bar under the heading of Other is where you can find a whole host of other incredibly useful information and features - such as logging to tell you who updated that IP range recently, thru custom fields that allow you to extend the data model to suit your own environment, and custom links to external applications. You can add in integrations such as web hooks to trigger certain actions - for example to make a call to an external automation engine to automatically provision a new vlan when it has been added to the NetBox database! You can also create reports and add custom scripts to extend the functionality of NetBox even further - the possibilities are literally endless!

So that's a super quick overview of the Web UI, and if we go back to the main home page, you can also access the same options via the main body of the page. plus you have a view of the change log which is incredibly useful to have right on the home page. 

There is a search bar at the top that allows you to search for any object in the the NetBox database, and you can either search within all objects or you can be more specific and filter for only the object type you need, for example  if you wanted to find all of your circuits provided by Level 3, you select 'providers, enter level 3 and this will return the level 3 provider and we can see that there are 13 circuits with Level 3, and if we click on the link it will take us to a list of those circuit objects. 

As you can see clicking on any hyperlink will take you to the related objects, for example if you click on the first circuit returned in the list, it displays all the related information for that circuit - for example the type of circuit, in this case it's MPLS and the status is Active you can see the circuit termination details on the right hand side. 

Also, right down at the footer of the page, are handy links to the official documentation, the REST and GrapghQL API documenatation, the source code and the community Slack channel.  And lastly of all this wasn't enough you can even switch the UI to Dark Mode! 

I hope that has been a useful introduction to the NetBox UI, and thanks for watching!