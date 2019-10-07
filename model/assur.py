import time


class Assurance:
    def __init__(self,app):
        self.app = app
    def unlock_step(self,i):
        steps_pass = {
            2: 'beFsRcTnLF',
            3: 'elC1oDfc41',
            4: 'n9vNSqy5nm',
            5: 'GhZLM6AZs6',
            6: 'DQEDfQ6uID',

        }

        self.app.driver.find_element_by_css_selector('a.action-unlock').click()
        time.sleep(2)
        self.app.driver.find_element_by_css_selector('#unlock-form input.password')\
            .send_keys(['{}'.format(steps_pass[i])])
        self.app.driver.find_element_by_css_selector('#unlock-form .btn.btn-submit').click()
        time.sleep(2)

    def filtering_links_for_Internal_and_external(self, links, dev):
        internal = []
        external = []
        for p in links:
            if p.startswith('https://'):
                internal.append(p)
            elif p.startswith('/'):
                internal.append('https://' + dev + p)
            elif p.startswith('#'):
                external.append(p)
        return({'internal':internal,'external':external})