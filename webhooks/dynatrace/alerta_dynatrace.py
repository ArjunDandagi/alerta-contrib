
from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase
import json

class DynatraceWebhook(WebhookBase):

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
            resource="UKGR",
            event="dynatrace_alert",
            environment="Production",
            severity="critical",
            service=["dynatrace"],
            group="Application",
            value="sample",
            text="something is missing",
            tags=list(),
            origin="Dynatrace",
            raw_data=json.dumps(payload)
        )

