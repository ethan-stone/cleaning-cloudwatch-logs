import { Duration, Stack, StackProps } from "aws-cdk-lib";
import { Construct } from "constructs";
import { Code, Function, Runtime } from "aws-cdk-lib/aws-lambda";
import { join } from "path";
import AdmZip from "adm-zip";
import { Effect, PolicyStatement } from "aws-cdk-lib/aws-iam";

export class InfraStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const zip = new AdmZip();
    zip.addLocalFile(join(__dirname, "../../index.py"));
    zip.writeZip(join(__dirname, "index.zip"));

    const cleanCloudwatchLogsFunction = new Function(
      this,
      "CleanCloudwatchLogs",
      {
        runtime: Runtime.PYTHON_3_9,
        handler: "index.handler",
        code: Code.fromAsset(join(__dirname, "index.zip")),
        timeout: Duration.seconds(60)
      }
    );

    cleanCloudwatchLogsFunction.addToRolePolicy(
      new PolicyStatement({
        effect: Effect.ALLOW,
        actions: [
          "logs:DescribeLogGroups",
          "logs:DescribeLogStreams",
          "logs:DeleteLogGroup"
        ],
        resources: ["*"]
      })
    );
  }
}
