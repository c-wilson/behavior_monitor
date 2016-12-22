import requests


def test():

    test_params = {'rig': 'T',
                   'status': 'Running',
                   'non_resp': 26,
                   'corr_resp': 100,
                   'n_trials': 300,
                   'vnc_viewer_url': 'none'}

    r = requests.post('http://10.162.44.252:8000/rig_status/update_status/',
                      data=test_params)
    print(r.url)

    return r.status_code


if __name__ == '__main__':
    print(test())