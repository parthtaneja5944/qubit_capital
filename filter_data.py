def clean_description(description):
    if description:
        return description.strip()
    return description

def filter_data(result):
    filtered_data = []
    print("filter1")
    data = result.get('data', [])
    print("filter2")
    for item_data in data:
        item = item_data.get('data', {})
        filtered_item = {
            'company_id': item.get('companyId'),
            'company_name': item.get('companyName'),
            'employee_count_range': item.get('employeeCount'),
            'call_to_action': item.get('callToAction'),
            'specialities': item.get('specialities'),
            'tagline': item.get('tagline'),
            'follower_count': item.get('followerCount'),
            'original_cover_image': item.get('originalCoverImage'),
            'logo_resolution_result': item.get('logoResolutionResult'),
            'industry': item.get('industry'),
            'description': clean_description(item.get('description')),
            'website_url': item.get('websiteUrl'),
            'headquarter': item.get('headquarter'),
            'founded_on': item.get('foundedOn'),
            'universal_name': item.get('universalName'),
            'url': item.get('url'),
        }
        filtered_data.append(filtered_item)

    return filtered_data    
