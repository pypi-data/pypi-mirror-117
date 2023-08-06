'''
# replace this
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.aws_ec2
import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.core


class FlywayConstruct(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="flywaymigrationconstruct.FlywayConstruct",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        vpc: aws_cdk.aws_ec2.IVpc,
        subnet: aws_cdk.aws_ec2.SubnetSelection,
        security_groups: typing.Mapping[typing.Any, typing.Any],
        bucket: aws_cdk.aws_s3.IBucket,
        migration_bucket_secret_arn: builtins.str,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param vpc: -
        :param subnet: -
        :param security_groups: -
        :param bucket: -
        :param migration_bucket_secret_arn: -
        '''
        jsii.create(FlywayConstruct, self, [scope, id, vpc, subnet, security_groups, bucket, migration_bucket_secret_arn])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bucketCodeArn")
    def bucket_code_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketCodeArn"))

    @bucket_code_arn.setter
    def bucket_code_arn(self, value: builtins.str) -> None:
        jsii.set(self, "bucketCodeArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="flywayLambdaMigration")
    def flyway_lambda_migration(self) -> aws_cdk.aws_lambda.Function:
        return typing.cast(aws_cdk.aws_lambda.Function, jsii.get(self, "flywayLambdaMigration"))

    @flyway_lambda_migration.setter
    def flyway_lambda_migration(self, value: aws_cdk.aws_lambda.Function) -> None:
        jsii.set(self, "flywayLambdaMigration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="handler")
    def handler(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "handler"))

    @handler.setter
    def handler(self, value: builtins.str) -> None:
        jsii.set(self, "handler", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idLambdaCode")
    def id_lambda_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idLambdaCode"))

    @id_lambda_code.setter
    def id_lambda_code(self, value: builtins.str) -> None:
        jsii.set(self, "idLambdaCode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="objectCodeKey")
    def object_code_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectCodeKey"))

    @object_code_key.setter
    def object_code_key(self, value: builtins.str) -> None:
        jsii.set(self, "objectCodeKey", value)


__all__ = [
    "FlywayConstruct",
]

publication.publish()
