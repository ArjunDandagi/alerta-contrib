
from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase
import json

class SplunkWebhook(WebhookBase):

    def incoming(self, query_string, payload):
        # return Alert(
        #     resource=payload['culprit'],
        #     event=payload['event']['event_id'],
        #     environment=environment,
        #     severity=severity,
        #     service=[payload['project']],
        #     group='Application',
        #     value=payload['level'],
        #     text='{} {}'.format(payload['message'], payload['url']),
        #     tags=['{}={}'.format(k, v) for k, v in payload['event']['tags']],
        #     attributes={'modules': ['{}=={}'.format(k, v) for k, v in payload['event']['modules'].items()]},
        #     origin='sentry.io',
        #     raw_data=str(payload)
        # )
        return Alert(
            resource="splunk",
            event=str(payload["search_name"]),
            environment="Production",
            severity="critical",
            service=[str(payload["app"])],
            group="Application",
            text=str(payload["search_name"]),
            tags=list(),
            origin="splunk",
            raw_data=json.dumps(payload)
        )

