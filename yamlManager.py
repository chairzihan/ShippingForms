from saveYaml import load_config, save_config

def add_sender(new_sender):
    data = load_config() or {}
    if 'senders' not in data or data['senders'] is None:
        data['senders'] = []
    data['senders'].append(new_sender)
    save_config(data)


def add_receiver(new_receiver):
    data = load_config() or {}
    if 'receivers' not in data or data['receivers'] is None:
        data['receivers'] = []
    data['receivers'].append(new_receiver)
    save_config(data)


def get_senders():
    data = load_config() or {}
    return data.get('senders', [])


def get_receivers():
    data = load_config() or {}
    return data.get('receivers', [])
