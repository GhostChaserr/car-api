


# Filter by listField
Channel.objects(tags__contains='music')

# Partial update
Channel.objects(_id=channel_id).update(
  set__name= channel_payload.name,
  set__summary=channel_payload.summary,
  set__tags= channel_payload.tags
)

# Add new value to list field
Channel.objects(pk=channel_id).update(add_to_set__followers = [user_id]);

# Sorting documents
Channel.objects.order_by('last_name', '-age')

# Access Pymongo directly
collection = Person._get_collection()
collection.find_one()

# Query unique fields
Channel.objects.get(model=2013)

# Query multiple fields
Channel.objects(model=2013)


