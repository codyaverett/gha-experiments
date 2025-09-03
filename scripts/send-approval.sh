# Helper script to send approval events
# save as: scripts/send-approval.sh
#!/bin/bash

# Usage: ./send-approval.sh approval-received wait_123 john.doe

EVENT_TYPE="$1"
WAIT_ID="$2"
APPROVED_BY="$3"

curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/$GITHUB_REPOSITORY/dispatches" \
  -d "{
    \"event_type\": \"$EVENT_TYPE\",
    \"client_payload\": {
      \"wait_id\": \"$WAIT_ID\",
      \"approved_by\": \"$APPROVED_BY\",
      \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"
    }
  }"
