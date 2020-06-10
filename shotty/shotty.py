import boto3

#abrindo uma ssesao no aws

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

def list_instances():
    for i in ec2.instances.all():
        tags = i.tags
        print(tags,', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name
        ))) 
    return

if __name__ == '__main__':
    list_instances()
    
    



 